from typing import List, Optional, Callable
import re
import os

STEP_RIGHT = 3
STEP_DOWN = 1


def process_input(file_name):
    with open(file_name) as report:
        return [line.strip() for line in report]


def next_pos(position: int, mod: int) -> int:
    return (position + STEP_RIGHT) % mod


def count_trees(maze: List[str]) -> int:
    tree_count = 0
    check_pos = STEP_RIGHT
    maze_row_len = len(maze[0])
    for row in maze[1:]:
        if row[check_pos] == "#":
            tree_count += 1
        check_pos = next_pos(check_pos, maze_row_len)
    return tree_count


if __name__ == "__main__":
    maze = process_input(os.path.join("src", "day_3", "input.in"))
    print(count_trees(maze))