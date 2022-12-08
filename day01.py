from collections import defaultdict
from typing import List, Dict
from pathlib import Path
from utils import read_lines


def parse_input(input_lines: List[str]) -> Dict[int, List[int]]:
    elf_meals = defaultdict(list)

    elf_number = 0
    for line in input_lines:

        if line == "\n":
            elf_number += 1
        else:
            elf_meals[elf_number].append(int(line))

    return elf_meals


def get_total_sorted_calories(elf_meals: Dict[int, List[int]]) -> List[int]:
    total_calories = []
    for elf, meals in elf_meals.items():
        total_calories.append(sum(meals))

    total_calories = sorted(total_calories, reverse=True)
    return total_calories


if __name__ == "__main__":
    puzzle_part1_path = Path('day01_part1.txt')
    lines = read_lines(puzzle_part1_path)
    puzzle_input = parse_input(lines)
    puzzle_solution = get_total_sorted_calories(puzzle_input)

    print(f"Part1 solution: {puzzle_solution[0]}")
    print(f"Part2 solution: {sum(puzzle_solution[:3])}")
