from typing import List, Dict, Tuple
import os, re
from functools import reduce
import math
import itertools

VALID_INSTRUCTIONS = {
    "acc": lambda x, y: (x + y, 1),
    "jmp": lambda x, y: (x, y),
    "nop": lambda x, y: (x, 1),
}


def process_input(file_name):
    with open(file_name) as report:
        result = []
        for line in report:
            instr, arg = line.strip().split(" ")
            result.append((instr, int(arg)))
        return result


def find_accumulator(instructions: List) -> int:
    accumulator = 0
    visited_instructions = set()
    instr_ptr = 0
    for _ in instructions:
        instr = instructions[instr_ptr]
        cmd, arg = instr
        if (cmd, arg, instr_ptr) in visited_instructions:
            return accumulator
        visited_instructions.add((*instr, instr_ptr))
        if not cmd in VALID_INSTRUCTIONS:
            raise Exception(f"Invalid Instruction {cmd} in a list")
        accumulator, ip_value = VALID_INSTRUCTIONS[cmd](accumulator, arg)
        instr_ptr += ip_value
    return accumulator


if __name__ == "__main__":
    instructions = process_input(os.path.join("src", "day_8", "input.in"))
    print(find_accumulator(instructions))
