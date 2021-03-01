from typing import List, Optional, Callable, Tuple, Dict
import os
import re

PASSPORT_FIELDS = {
    "byr": lambda x: True if int(x) >= 1920 and int(x) <= 2002 else False,
    "iyr": lambda x: True if int(x) >= 2010 and int(x) <= 2020 else False,
    "eyr": lambda x: True if int(x) >= 2020 and int(x) <= 2030 else False,
    "hgt": lambda x: check_hgt(x),
    "hcl": lambda x: check_hcl(x),
    "ecl": lambda x: check_ecl(x),
    "pid": lambda x: check_pid(x),
    "cid": lambda x: True,
}

OPTIONAL_FIELDS = ["cid"]


def process_input(file_name):
    result = []
    with open(file_name) as report:
        passports = [line.replace("\n", " ") for line in report.read().split("\n\n")]
        for line in passports:
            single_passport = dict(info.split(":") for info in line.split(" "))
            result.append(single_passport)
    return result


def check_hgt(data: str):
    field = re.match(r"(\d+)cm$", data)
    if field:
        value = int(field.group(1))
        if value >= 150 and value <= 193:
            return True
    field = re.match(r"(\d+)in$", data)
    if field:
        value = int(field.group(1))
        if value >= 59 and value <= 76:
            return True
    return False


def check_hcl(data: str):
    field = re.match(r"#([0-9a-f]{6}$)", data)
    if field:
        return True
    return False


def check_ecl(data: str):
    field = re.match(r"amb$|blu$|brn$|gry$|grn$|hzl$|oth$", data)
    if field:
        return True
    return False


def check_pid(data):
    field = re.match(r"(\d){9}$", data)
    if field:
        return True
    return False


def validate_fields(passport: Dict) -> bool:
    return all([PASSPORT_FIELDS[str(k)](v) for k, v in passport.items()])


def get_valid_passsports_part_1(passports: List) -> int:
    count = 0
    keys_to_exists = set(
        [k for k in PASSPORT_FIELDS.keys() if k not in OPTIONAL_FIELDS]
    )
    for elem in passports:
        elem_set = set([k for k, v in elem.items()])
        if keys_to_exists.issubset(elem_set):
            count += 1
    return count


def get_valid_passsports_part_2(passports: List) -> int:
    count = 0
    keys_to_exists = set(
        [k for k in PASSPORT_FIELDS.keys() if k not in OPTIONAL_FIELDS]
    )
    for elem in passports:
        elem_set = set([k for k, v in elem.items()])
        if keys_to_exists.issubset(elem_set) and validate_fields(elem):
            count += 1
    return count


if __name__ == "__main__":
    passport_list = process_input(os.path.join("src", "day_4", "input.in"))
    print(get_valid_passsports_part_1(passport_list))
    print(get_valid_passsports_part_2(passport_list))
