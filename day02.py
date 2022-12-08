from typing import List
import re
from utils import read_lines
from pathlib import Path


def parse_input(input_lines: List[str]) -> List[List[str]]:
    game_rounds = []
    for line in input_lines:
        current_round = re.findall(r"[A-Z]", line)
        game_rounds.append(current_round)
    return game_rounds


def get_game_rounds_scores(game_rounds: List[List[str]], part2: bool) -> List[int]:
    game_rounds_scores = []
    for game_round in game_rounds:
        game_rounds_scores.append(get_round_score(game_round, part2))

    return game_rounds_scores


def get_player_2_move(player_1_move: int, player_2_strategy: str) -> int:
    player_2_move = None
    if player_2_strategy == 'X':
        # We should lose
        player_2_move = ((player_1_move + 2) - 1) % 3 + 1
    elif player_2_strategy == 'Y':
        # Draw
        player_2_move = player_1_move
    elif player_2_strategy == 'Z':
        # We should win
        player_2_move = ((player_1_move + 1) - 1) % 3 + 1

    return player_2_move


def get_round_score(round: List[str], part2: bool) -> int:
    player_1_move = ord(round[0]) - ord('A') + 1
    if part2:
        # Part 2 solution
        player_2_move = get_player_2_move(player_1_move, round[1])
    else:
        # Part 1 solution
        player_2_move = ord(round[1]) - ord('X') + 1

    score = player_2_move
    difference = player_2_move - player_1_move
    if difference % 3 == 1:
        # We won
        score += 6
    elif difference % 3 == 2:
        # We lost
        pass
    elif difference == 0:
        # Draw
        score += 3

    return score


if __name__ == "__main__":
    puzzle_part1_path = Path('day02_part1.txt')
    puzzle_lines = read_lines(puzzle_part1_path)
    puzzle_input = parse_input(puzzle_lines)
    game_rounds_scores_part1 = get_game_rounds_scores(puzzle_input, False)
    game_rounds_scores_part2 = get_game_rounds_scores(puzzle_input, True)

    print(f"Part 1 solution: {sum(game_rounds_scores_part1)}")
    print(f"Part 2 solution: {sum(game_rounds_scores_part2)}")
