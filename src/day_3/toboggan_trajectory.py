from typing import List, Optional, Callable, Tuple
import os
from functools import reduce


def process_input(file_name):
    with open(file_name) as report:
        return [line.strip() for line in report]


def next_pos(position: int, mod: int, step: int) -> int:
    return (position + step) % mod


def count_trees(maze: List[str], slope: Tuple) -> int:
    tree_count = 0
    step = slope[0]
    check_pos = step
    maze_row_len = len(maze[0])
    for i in range(0, len(maze) - 1, slope[1]):
        if maze[i + slope[1]][check_pos] == "#":
            tree_count += 1
        check_pos = next_pos(check_pos, maze_row_len, step)
    return tree_count


if __name__ == "__main__":
    maze = process_input(os.path.join("src", "day_3", "input.in"))
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    reduce(lambda x, y: x * y, [count_trees(maze, slope) for slope in slopes])
