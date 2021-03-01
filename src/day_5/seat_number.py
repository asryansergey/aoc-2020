from typing import List, Optional
import os
from functools import reduce
import math
import itertools


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


def get_seat_ids(encoded_seats: List[str]) -> int:
    seat_ids = []
    for seat in encoded_seats:
        row, col = decode_seat_number(seat)
        seat_ids.append(compute_seat_id(row, col))
    return seat_ids


def get_target_seat_id(encoded_seats: List[str]) -> Optional[int]:
    excluded_seats = [
        "FFFFFFF" + "".join(x) for x in itertools.product(["L", "R"], repeat=3)
    ]
    excluded_seats.extend(
        ["BBBBBBB" + "".join(x) for x in itertools.product(["L", "R"], repeat=3)]
    )
    excluded_seat_ids = set(get_seat_ids(excluded_seats))
    seat_ids = sorted(get_seat_ids(encoded_seats))
    candidate_ids = set([x + 1 for x, y in zip(seat_ids, seat_ids[1:]) if y - x == 2])
    target_elem = candidate_ids - excluded_seat_ids
    if target_elem:
        return target_elem.pop()
    return None


if __name__ == "__main__":
    seats_encoded = process_input(os.path.join("src", "day_5", "input.in"))
    max_seat_id = max(get_seat_ids(seats_encoded))
    print(max_seat_id)
    print(get_target_seat_id(seats_encoded))