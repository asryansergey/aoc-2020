from typing import List, Dict, Optional
import os

MAX_JOLTAGE_DIFF = 3


def process_input(file_name):
    with open(file_name) as report:
        return [int(line.strip()) for line in report]


def find_target_number(jolts_list: List[int]) -> Optional[int]:
    jolts_diff_result = {k: [] for k in range(1, MAX_JOLTAGE_DIFF + 1)}  # type: ignore
    jolts_list.sort()
    built_in_joltage = jolts_list[-1]
    jolts_diff_result[3] += [built_in_joltage]
    for idx, elem in enumerate(jolts_list, 1):
        if idx >= len(jolts_list):
            break
        diff = jolts_list[idx] - elem
        jolts_diff_result[diff].append(jolts_list[idx])

    return len(jolts_diff_result[1]) * len(jolts_diff_result[3])


def adapters_distinct_arrangement_count(jolts_list: List[int]) -> int:
    jolts_diff_result = [1]
    jolts_list.sort()
    built_in_joltage_rate = jolts_list[-1] + 3
    for idx in range(1, built_in_joltage_rate + 1):
        if not idx in jolts_list and idx != built_in_joltage_rate:
            jolts_diff_result.append(0)
        else:
            curr_val = jolts_diff_result[idx - 1]
            if idx >= 2:
                curr_val += jolts_diff_result[idx - 2]
            if idx >= 3:
                curr_val += jolts_diff_result[idx - 3]
            jolts_diff_result.append(curr_val)

    return jolts_diff_result[-1]


if __name__ == "__main__":
    jolts_list = process_input(os.path.join("src", "day_10", "input.in"))
    null_joltage_rate = [0]
    print(find_target_number(jolts_list + null_joltage_rate))
    print(adapters_distinct_arrangement_count(jolts_list))
