from typing import List, Optional
import os


def process_input(file_name):
    with open(file_name) as report:
        return [int(line.strip()) for line in report]


def find_target_number() -> Optional[int]:
    ...


if __name__ == "__main__":
    number_list = process_input(os.path.join("src", "day_9", "input.in"))
    print(find_target_number(number_list))