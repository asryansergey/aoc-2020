from typing import List, Dict
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
                re.split(r"\d ", x)[1].split("bag")[0].strip()
                for x in line.split("contain")[1].strip()[:-1].split(",")
                if re.search(r"\d", x)
            ]
            result[key] = bag_list
        return result


def find_shiny_gold(search_list: List[str], bags_dict: Dict) -> int:
    for idx, elem in enumerate(search_list):
        for k, bags in bags_dict.items():
            if elem in bags:
                search_list.append(k)
                bags_dict.pop(k)
                return find_shiny_gold(search_list, bags_dict) + 1
        search_list.remove(elem)
    return 0


def count_shiny_gold_containers(bags: List) -> int:
    search_list = ["shiny gold"]
    return find_shiny_gold(search_list, bags)


if __name__ == "__main__":
    baggage_list = process_input(os.path.join("src", "day_7", "input.in"))
    print(count_shiny_gold_containers(baggage_list))