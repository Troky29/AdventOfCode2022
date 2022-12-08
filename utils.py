from pathlib import Path
from typing import List


def read_lines(path: Path) -> List[str]:
    lines = None
    with open(path, 'r') as f:
        lines = f.read().splitlines()

    return lines
