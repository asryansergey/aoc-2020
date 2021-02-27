from typing import List, Optional, Callable
import re
import os


def process_input(file_name):
    with open(file_name) as report:
        return [line.strip() for line in report]


if __name__ == "__main__":
    maze = process_input(os.path.join("src", "day_3", "input.in"))
