from typing import List, Optional
import os, re
from functools import reduce
import math
import itertools


def process_input(file_name):
    """
    create dict with the following structure:
    {
        "bag_name" : [list of bags it contains]
        ...
    }
    First search for "shiny gold" bag, count those bags and
    adding those in a list for further search e.g.
    "X" bag containg "shiny gold" bag
    add "X" bag to a list and after finding all "shiny gold" bag
    search for bags containing "X" bag and so on untill all bags
    are scanned.
    """
    result = {}
    with open(file_name) as report:
        for line in report.readlines():
            key = line.split("contain")[0].strip()
            bag_list = [
                re.split(r"\d ", x)[1]
                for x in line.split("contain")[1].strip()[:-1].split(",")
                if re.search(r"\d", x)
            ]
            result[key] = bag_list
        return result


def count_shiny_gold_containers(bags: List) -> int:
    ...


if __name__ == "__main__":
    baggage_list = process_input(os.path.join("src", "day_7", "input.in"))
    print(baggage_list)