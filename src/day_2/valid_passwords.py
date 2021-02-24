from typing import List, Optional, Callable
import re
import os


def process_input(file_name):
    with open(file_name) as report:
        return [line.strip() for line in report]


def is_valid_passwords_in_range(range_min, range_max, symbol, text):
    if len(re.findall(f"{symbol}", text)) in range(range_min, range_max + 1):
        return True
    return False


def is_valid_passwords_in_postion(pos_1, pos_2, symbol, text):
    char_1, char_2 = (text[i - 1] for i in [pos_1, pos_2])
    if char_1 != char_2 and any(symbol == char for char in [char_1, char_2]):
        return True
    return False


def get_valid_passvords(
    pwsd_list: List[int], is_valid: Callable[..., Optional[int]]
) -> Optional[int]:
    valid_pswd_count = 0
    for pswd in pwsd_list:
        data = (line for line in pswd.split(" "))
        range_min, range_max = (int(num) for num in re.split(r"\-", next(data)))
        symbol = next(data).split(":")[0]
        text = next(data).strip()
        if is_valid(range_min, range_max, symbol, text):
            valid_pswd_count += 1
    return valid_pswd_count if valid_pswd_count else None


if __name__ == "__main__":
    password_list = process_input(os.path.join("src", "day_2", "input.in"))
    print(
        f"Valid passwords count is: {get_valid_passvords(password_list, is_valid_passwords_in_range)}"
    )
    print(
        f"Valid passwords count is: {get_valid_passvords(password_list, is_valid_passwords_in_postion)}"
    )
