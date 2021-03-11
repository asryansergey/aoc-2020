from typing import List, Dict, Tuple, NoReturn
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
        for idx, line in enumerate(report):
            instr, arg = line.strip().split(" ")
            result.append((instr, int(arg), idx))
        return result


def find_accumulator_part_1(instructions: List) -> int:
    accumulator = 0
    visited_instructions = set()
    instr_ptr = 0
    for _ in instructions:
        instr = instructions[instr_ptr]
        cmd, arg, _ = instr
        if (cmd, arg, instr_ptr) in visited_instructions:
            return accumulator, False
        visited_instructions.add((cmd, arg, instr_ptr))
        if not cmd in VALID_INSTRUCTIONS:
            raise Exception(f"Invalid Instruction {cmd} in a list")
        accumulator, ip_value = VALID_INSTRUCTIONS[cmd](accumulator, arg)
        instr_ptr += ip_value
        if instr_ptr == len(instructions):
            print("Last instruction executed!")
            return accumulator, True
    return accumulator, True


def swap_nop_and_jmp(instructions: List, instr_to_replace: Tuple) -> NoReturn:
    cmd = "nop" if instr_to_replace[0] == "jmp" else "jmp"
    new_instr = (cmd, instr_to_replace[1], instr_to_replace[2])
    instructions.remove(instr_to_replace)
    pos = instr_to_replace[2]
    instructions.insert(pos, new_instr)


def find_accumulator_without_loop(instruction: List) -> int:
    status = False
    for i in range(len(instructions)):
        elem = instructions[i]
        if elem[0] == "jmp" and elem[1] < 0:
            swap_nop_and_jmp(instructions, elem)
            res, status = find_accumulator_part_1(instructions)
            elem = instructions[i]
            swap_nop_and_jmp(instructions, elem)
        if elem[0] == "nop" and elem[1] > 0:
            swap_nop_and_jmp(instructions, elem)
            res, status = find_accumulator_part_1(instructions)
            elem = instructions[i]
            swap_nop_and_jmp(instructions, elem)
        if status:
            print(f"Accumulator value: {res}")
            break


if __name__ == "__main__":
    instructions = process_input(os.path.join("src", "day_8", "input.in"))
    print(find_accumulator_part_1(instructions))
    find_accumulator_without_loop(instructions)
