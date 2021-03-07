from typing import List, Dict, Tuple
import os, re
from functools import reduce
import math
import itertools


def process_input(file_name):
    result = {}
    with open(file_name) as report:
        for line in report.readlines():
            key = line.split("contain")[0].split("bag")[0].strip()
            bag_list = [
                (
                    int(re.split(r"(\d )", x)[1].strip()),
                    re.split(r"(\d )", x)[2].split("bag")[0].strip(),
                )
                for x in line.split("contain")[1].strip()[:-1].split(",")
                if re.search(r"\d", x)
            ]
            result[key] = bag_list
        return result


def find_shiny_gold(search_list: List[str], bags_dict: Dict[str, List[Tuple]]) -> int:
    for elem in search_list:
        for k, bags in bags_dict.items():
            if [x for x in bags if elem in x[1]]:
                search_list.append(k)
                bags_dict.pop(k)
                return find_shiny_gold(search_list, bags_dict) + 1
        search_list.remove(elem)
    return 0


def find_bags_inside_shiny_gold(search_list: List, bags_dict: Dict) -> int:
    result = 0
    while len(search_list):
        child_sum = result
        root = search_list.pop(0)
        queue = bags_dict[root[1]]
        for elem in queue:
            child_sum += elem[0] * (find_bags_inside_shiny_gold([elem], bags_dict) + 1)
        result += child_sum
    return result


def count_shiny_gold_containers(bags_dict: Dict) -> int:
    search_list = ["shiny gold"]
    return find_shiny_gold(search_list, bags_dict)


def count_bags_inside_shiny_gold(bags_dict: Dict) -> int:
    search_list = [(1, "shiny gold")]
    return find_bags_inside_shiny_gold(search_list, bags_dict)


if __name__ == "__main__":
    baggage_list = process_input(os.path.join("src", "day_7", "input.in"))
    print(count_shiny_gold_containers(baggage_list))
    print(count_bags_inside_shiny_gold(baggage_list))