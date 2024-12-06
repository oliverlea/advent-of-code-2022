
from typing import List
from utils import read_file

def score(x: str) -> int:
    if x.upper() == x:
        return 27 + (ord(x)) - ord('A')
    return 1 + (ord(x) - ord('a'))


def part2(lines: List[str]) -> int:
    def determine_badge(start: int) -> str:
        x = set(lines[start])
        for i in range(1, 3):
            x = x.intersection(set(lines[start + i]))
        return x.pop()
    result = 0
    for i in range(0, len(lines), 3):
        x = determine_badge(i)
        result += score(x)
    return result


def part1(lines: List[str]) -> int:
    result = 0
    for line in lines:
        xs = set(line[:len(line) // 2])
        ys = set(line[len(line) // 2:])
        for x in xs:
            if x in ys:
                result += score(x)
                break
    return result

if __name__ == '__main__':
    lines = [x.strip() for x in read_file('day03.txt')]
    print(part1(lines))
    print(part2(lines))