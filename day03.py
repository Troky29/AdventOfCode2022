import itertools
from pathlib import Path
from typing import List
from utils import read_lines


def parse_input(input_lines: List[str]) -> List[List[str]]:
    rucksacks = []
    for line in input_lines:
        rucksack = []
        for char in line:
            rucksack.append(char)
        rucksacks.append(rucksack)

    return rucksacks


def get_misplaced_items(rucksacks: List[List[str]]) -> List[str]:
    misplaced_items = []
    for rucksack in rucksacks:
        compartment_size = len(rucksack) // 2
        first_half = set(rucksack[:compartment_size])
        second_half = set(rucksack[compartment_size:])

        misplaced_item = first_half.intersection(second_half)
        misplaced_items.append(misplaced_item.pop())

    return misplaced_items


def get_items_priority(misplaced_items: List[str]) -> List[int]:
    priority = {chr(key): value + 1 for (value, key) in
                enumerate(itertools.chain(range(ord('a'), ord('z') + 1), range(ord('A'), ord('Z') + 1)))}
    misplaced_items_priority = []
    for misplaced_item in misplaced_items:
        misplaced_items_priority.append(priority[misplaced_item])

    return misplaced_items_priority


def get_missing_badges(rucksacks: List[List[str]]) -> List[str]:
    missing_badges = []
    for i in range(0, len(rucksacks), 3):
        missing_badge = set(rucksacks[i]).intersection(set(rucksacks[i + 1]).intersection(set(rucksacks[i + 2])))
        missing_badges.append(missing_badge.pop())

    return missing_badges


if __name__ == "__main__":
    # puzzle_lines = TEST.split('\n')
    puzzle_part1_path = Path('day03_part1.txt')
    puzzle_lines = read_lines(puzzle_part1_path)
    puzzle_input = parse_input(puzzle_lines)

    misplaced_items = get_misplaced_items(puzzle_input)
    misplaced_items_priority = get_items_priority(misplaced_items)

    missing_badges = get_missing_badges(puzzle_input)
    missing_badges_priority = get_items_priority(missing_badges)

    print(f"Part 1 solution: {sum(misplaced_items_priority)}")
    print(f"Part 2 solution: {sum(missing_badges_priority)}")
