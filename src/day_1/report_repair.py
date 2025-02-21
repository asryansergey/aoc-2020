from typing import List, Optional
import os


def process_input(file_name):
    with open(file_name) as report:
        return [int(num.strip()) for num in report]


def sum_to_2020_part_1(expence_report: List[int]) -> Optional[List[int]]:
    expence_report.sort()
    for idx, x in enumerate(expence_report):
        for _, y in enumerate(expence_report, idx + 1):
            if x + y == 2020:
                print(f"Found correct values {x} and {y}: x * y = ", x * y)
                return [x, y]
            if x + y > 2020:
                break
    return None


def sum_to_2020_part_2(expence_report: List[int]) -> Optional[List[int]]:
    expence_report.sort()
    for idx_x, x in enumerate(expence_report):
        for idx_y, y in enumerate(expence_report, idx_x + 1):
            if x + y > 2020:
                break
            for idx_z, z in enumerate(expence_report, idx_y + 1):
                if y + z > 2020 or x + y + z > 2020:
                    break
                if x + y + z == 2020:
                    print(
                        f"Found correct values {x}, {y} and {z}: x * y * z = ",
                        x * y * z,
                    )
                    return [x, y, z]
    return None


def sum_to_2020_part_2_opt(expence_report: List[int]) -> Optional[List[int]]:
    expence_report.sort()

    hashmap = {}
    for i, elem in enumerate(expence_report):
        hashmap[elem] = i

    for i in range(len(expence_report)):
        for j in range(i + 1, len(expence_report)):
            if expence_report[i] + expence_report[j] > 2020:
                break
            search_elem = 2020 - (expence_report[i] + expence_report[j])
            if search_elem in hashmap and hashmap[search_elem] > j:
                print(
                    "Found the correct values: x * y * z = ",
                    expence_report[i] * expence_report[j] * search_elem,
                )
                return [expence_report[i], expence_report[j], search_elem]
    return None


if __name__ == "__main__":
    expence_report = process_input(os.path.join("src", "day_1", "input.in"))
    sum_to_2020_part_1(expence_report)
    sum_to_2020_part_2(expence_report)
    sum_to_2020_part_2_opt(expence_report)
