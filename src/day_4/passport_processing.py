from typing import List, Optional, Callable, Tuple
import os


def process_input(file_name):
    result = []
    with open(file_name) as report:
        passports = [line.replace("\n", " ") for line in report.read().split("\n\n")]
        for line in passports:
            single_passport = dict(info.split(":") for info in line.split(" "))
            result.append(single_passport)
    return result


def get_valid_passsports(passports: List, mandatory_keys: List[str]) -> int:
    count = 0
    keys_to_exists = set(mandatory_keys)
    for elem in passports:
        elem_set = set([k for k, v in elem.items()])
        if keys_to_exists.issubset(elem_set):
            count += 1
    return count


if __name__ == "__main__":
    passport_list = process_input(os.path.join("src", "day_4", "input.in"))
    mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    print(get_valid_passsports(passport_list, mandatory_keys))
