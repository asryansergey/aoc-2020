from typing import List, Optional
import os
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
    result = []
    with open(file_name) as report:
        return [line.strip() for line in report]


if __name__ == "__main__":
    baggage_list = process_input(os.path.join("src", "day_7", "input.in"))
    ...