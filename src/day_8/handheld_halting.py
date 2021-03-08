from typing import List, Dict, Tuple
import os, re
from functools import reduce
import math
import itertools


def process_input(file_name):
    with open(file_name) as report:
        return [line.strip() for line in report]


def find_accumulator(instr: List) -> int:
    ...


if __name__ == "__main__":
    instructions = process_input(os.path.join("src", "day_8", "input.in"))
    print(find_accumulator(instructions))