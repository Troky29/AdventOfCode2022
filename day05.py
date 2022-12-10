import copy
from collections import defaultdict
from pathlib import Path
from typing import List, Dict, Tuple, Any
from utils import read_lines
import re

def parse_stacks(setup_lines: List[str], len_numbers: int) -> Dict[int, List[int]]:
    stacks = defaultdict(list)
    for line in setup_lines:
        for i in range(0, len_numbers):
            char = re.search(r"[A-Z]", line[i * 4:(i + 1) * 4])
            if char:
                stacks[i+1].append(char.group(0))

    # Reverse the order of all stacks
    [stack.reverse() for stack in stacks.values()]
    return stacks


def parse_input(input_lines: List[str]):
    stacks = None
    moves = []

    # Parse initial stacks
    setup_lines_count = 0
    for line in input_lines:
        numbers = re.findall(r"\d+", line)
        if len(numbers) == 0:
            setup_lines_count += 1
        else:
            stacks = parse_stacks(input_lines[:setup_lines_count], len(numbers))
            break

    # Parse moves
    for line in input_lines[setup_lines_count + 2:]:
        moves.append(re.findall(r"\d+", line))

    return stacks, moves


def make_move(stacks: defaultdict[int, List[int]], move: List[int], reverse: bool = True):
    times, move_from, move_to = [int(m) for m in move]
    moved_boxes = [stacks[move_from].pop() for _ in range(times)]
    if not reverse:
        moved_boxes.reverse()

    stacks[move_to] += moved_boxes
    return


def make_moves(original_stacks: defaultdict[int, List[int]], moves: List[List[int]], reverse: bool = True):
    stacks = copy.deepcopy(original_stacks)
    for move in moves:
        make_move(stacks, move, reverse)

    return stacks

def get_top_crates(stacks: defaultdict[int, List[int]]):
    return ''.join([stacks[i][-1] for i in range(1, len(stacks) + 1)])


if __name__ == "__main__":
    puzzle_part1_path = Path('day05.txt')
    puzzle_lines = read_lines(puzzle_part1_path)
    stacks, moves = parse_input(puzzle_lines)
    stacks_1 = make_moves(stacks, moves)
    stacks_2 = make_moves(stacks, moves, False)

    print(f"Part 1 solution: {get_top_crates(stacks_1)}")
    print(f"Part 2 solution: {get_top_crates(stacks_2)}")
