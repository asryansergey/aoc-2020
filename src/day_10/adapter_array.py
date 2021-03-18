from typing import List, Optional
import os

MAX_JOLTAGE_DIFF = 3


def process_input(file_name):
    with open(file_name) as report:
        return [int(line.strip()) for line in report]


def find_target_number(jolts_list: List[int]) -> Optional[int]:
    jolts_diff_result = {k: [] for k in range(1, MAX_JOLTAGE_DIFF + 1)}
    jolts_list.sort()
    built_in_joltage = jolts_list[-1]
    jolts_diff_result[3] += [built_in_joltage]
    for diff, _ in enumerate(jolts_diff_result.items(), 1):
        for idx, elem in enumerate(jolts_list, 1):
            if idx >= len(jolts_list):
                break
            if jolts_list[idx] - elem == diff:
                jolts_diff_result[diff].append(jolts_list[idx])

    return len(jolts_diff_result[1]) * len(jolts_diff_result[3])


if __name__ == "__main__":
    jolts_list = process_input(os.path.join("src", "day_10", "input.in"))
    null_jolt = [0]
    jolts_list += null_jolt
    print(find_target_number(jolts_list))
