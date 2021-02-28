from typing import List, Optional, Callable, Tuple
import os


def process_input(file_name):
    ...


def get_valid_passsports(passports: List) -> int:
    ...


if __name__ == "__main__":
    passport_list = process_input(os.path.join("src", "day_4", "input.in"))
    get_valid_passsports(passport_list)