from typing import List, Optional
import os
from functools import reduce
import math
import itertools


def process_input(file_name):
    result = []
    with open(file_name) as report:
        return [line.strip() for line in report]


if __name__ == "__main__":
    baggage_list = process_input(os.path.join("src", "day_6", "input.in"))
    ...