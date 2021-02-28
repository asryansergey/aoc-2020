from typing import List, Optional, Callable, Tuple
import os
import json


def process_input(file_name):
    result = []
    with open(file_name) as report:
        single_passport = {}
        passports = [line.strip("\n") for line in report.readlines()]
        for i, line in enumerate(passports):
            if line != "":
                for elem in line.split(" "):
                    pair = elem.split(":")
                    single_passport[pair[0]] = pair[1]
            if line == "" or i == len(passports) - 1:
                result.append(single_passport.copy())
                single_passport.clear()
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
