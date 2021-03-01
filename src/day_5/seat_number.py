from typing import List
import os
from functools import reduce
import math


def process_input(file_name):
    result = []
    with open(file_name) as report:
        return [line.strip() for line in report]


def compute_seat_id(row: int, col: int) -> int:
    return row * 8 + col


def decode_seat_number(single_seat: str) -> int:
    row_range = [0, 127]
    col_range = [0, 7]
    for idx, char in enumerate(single_seat):
        if idx < 7:
            if char == "F":
                row_range[-1] -= math.ceil(reduce(lambda x, y: y - x, row_range) / 2)
            else:
                row_range[0] += math.ceil(reduce(lambda x, y: y - x, row_range) / 2)
        else:
            if char == "L":
                col_range[-1] -= math.ceil(reduce(lambda x, y: y - x, col_range) / 2)
            else:
                col_range[0] += math.ceil(reduce(lambda x, y: y - x, col_range) / 2)
        col = col_range[0] | col_range[1]
    return row_range[0] | row_range[1], col_range[0] | col_range[1]


def get_max_seat_id(encoded_seats: List[str]) -> int:
    seat_ids = []
    for seat in encoded_seats:
        row, col = decode_seat_number(seat)
        seat_ids.append(compute_seat_id(row, col))
    return max(seat_ids)


if __name__ == "__main__":
    seats_encoded = process_input(os.path.join("src", "day_5", "input.in"))
    print(get_max_seat_id(seats_encoded))