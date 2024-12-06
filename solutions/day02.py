
from typing import List
from utils import read_file

BEATS = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

LOSES = {y: x for x, y in BEATS.items()}

def score(left: str, right: str) -> int:
    result = (ord(right) - ord('A')) + 1
    if left == right:
        return result + 3
    if BEATS[left] == right:
        return result
    return result + 6

def part1(lines: List[str]) -> int:
    def normalize(x: str) -> str:
        return chr(ord(x[0]) - (ord('X') - ord('A')))
    return sum(score(l[0], normalize(l[2])) for l in lines)

def part2(lines: List[str]) -> int:
    def translate(line: str) -> str:
        plays, strat = line[0], line[2]
        if strat == 'X':
            return f"{plays} {BEATS[plays]}"
        elif strat == 'Y':
            return plays + " " + plays
        return f"{plays} {LOSES[plays]}"
    translated = [translate(line) for line in lines]
    return sum(score(l[0], l[2]) for l in translated)

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day02.txt')]
    print(part1(lines))
    print(part2(lines))