from pathlib import Path
from typing import List, Dict, Tuple
import numpy as np
from utils import read_lines


def parse_input(input_lines: List[str]) -> List[Dict[int, List[int]]]:
    sectors_pairs = []

    def parse_range(pair: str) -> List[int]:
        range = pair.split('-')
        range = [int(range[0]), int(range[1])]
        range.sort()
        return range

    def parse_pair_ranges(line: str) -> Tuple[List[int], List[int]]:
        first_pair, secod_pair = line.split(',')
        return parse_range(first_pair), parse_range(secod_pair)

    for line in input_lines:
        first_range, second_range = parse_pair_ranges(line)
        sectors_pair = {0: first_range, 1: second_range}
        sectors_pairs.append(sectors_pair)

    return sectors_pairs


def is_range_contained(first_range: np.array, second_range: np.array) -> bool:
    return np.sign(np.prod(first_range - second_range)) <= 0

def is_range_intersection(first_range: np.array, second_range: np.array) -> bool:
    return np.sign(np.prod(first_range - second_range[::-1])) <= 0
def count_contained_range(pairs_ranges: List[Dict[int, List[int]]]) -> Tuple[int, int]:
    count_contained, count_intersecting = 0, 0
    for pair_ranges in pairs_ranges:
        first_range, second_range = np.array([x for x in pair_ranges.values()])
        if is_range_contained(first_range, second_range):
            count_contained += 1
            count_intersecting += 1
            continue

        if is_range_intersection(first_range, second_range):
            count_intersecting += 1

    return count_contained, count_intersecting


if __name__ == "__main__":
    puzzle_part1_path = Path('day04_part1.txt')
    puzzle_lines = read_lines(puzzle_part1_path)
    puzzle_input = parse_input(puzzle_lines)
    contained_count, intersecting_count = count_contained_range(puzzle_input)
    print(f"Part 1 solution: {contained_count}")
    print(f"Part 2 solution: {intersecting_count}")
