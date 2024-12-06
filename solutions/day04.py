
import re
from typing import List, Tuple
from utils import read_file, Loc

PARSE_REGEX = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

def parse(lines: List[str]) -> List[Tuple[Loc, Loc]]:
    def parse_line(l: str) -> Tuple[Loc, Loc]:
        match = PARSE_REGEX.match(l)
        if not match:
            raise ValueError()
        pair1 = int(match.group(1)), int(match.group(2))
        pair2 = int(match.group(3)), int(match.group(4))
        return (pair1, pair2)
    return [parse_line(line) for line in lines]


def part1(inputs: List[Tuple[Loc, Loc]]) -> int:
    result = 0
    for x, y in inputs:
        left = min(x[0], y[0])
        right = max(x[1], y[1])
        if (left, right) in (x, y):
            result += 1
    return result

def part2(inputs: List[Tuple[Loc, Loc]]) -> int:
    def overlaps(x: Loc, y: Loc) -> bool:
        if x[0] < y[0]:
            left = x
            right = y
        else:
            left = y
            right = x
        return left[1] >= right[0]
    return sum(1 for x, y in inputs if overlaps(x, y))

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day04.txt')]
    inputs = parse(lines)
    print(part1(inputs))
    print(part2(inputs))