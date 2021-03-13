from typing import List, Optional
import os

PREAMBLE_RANGE = 25


def process_input(file_name):
    with open(file_name) as report:
        return [int(line.strip()) for line in report]


def can_sum(preamble: List[int], target_num: int):
    if target_num < 0:
        return False
    if not target_num:
        return True
    for idx, num in enumerate(preamble, 1):
        next_num = target_num - num
        if can_sum(preamble[idx:], next_num):
            return True
    return False


def find_target_number(number_list: List[int]) -> Optional[int]:
    for idx in range(len(number_list[:-PREAMBLE_RANGE])):
        preamble = number_list[idx : idx + PREAMBLE_RANGE]
        target_num = number_list[idx + PREAMBLE_RANGE]
        if not can_sum(preamble, target_num):
            return target_num
    return None


def find_xmas_weakness(number_list: List[int], target_number: int) -> Optional[int]:
    target_index = number_list.index(target_number)
    start_pos = 0
    for start_pos, init_elem in enumerate(number_list[:target_index]):
        total_sum = 0
        contiguous_list = [init_elem]
        for idx in range(start_pos + 1, len(number_list[:target_index])):
            num = number_list[idx]
            total_sum += num
            if total_sum < target_number:
                contiguous_list.append(num)
            elif total_sum > target_number:
                contiguous_list = [contiguous_list[-1]]
            else:
                contiguous_list.sort()
                return contiguous_list[0] + contiguous_list[-1]
    return None


if __name__ == "__main__":
    number_list = process_input(os.path.join("src", "day_9", "input.in"))
    target_number = find_target_number(number_list)
    print(target_number)
    print(find_xmas_weakness(number_list, target_number))