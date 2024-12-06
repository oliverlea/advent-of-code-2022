
import re
from typing import List, Tuple
from utils import read_file, Loc

def parse_stacks(lines: List[str]) -> List[List[str]]:
    stacks: List[List[str]] = []
    lines = lines[::-1]
    for x in range(1, len(lines[0]), 4):
        s: List[str] = []
        for y in range(len(lines)):
            cur = lines[y][x]
            if cur != ' ':
                s.append(cur)
        stacks.append(s)
    return stacks

def parse_instructions(instructions: List[str]) -> List[Tuple[int, int, int]]:
    r = re.compile(r'move (\d+) from (\d+) to (\d+)')
    def extract(instruction: str) -> Tuple[int, int, int]:
        m = r.match(instruction) 
        if not m:
            raise ValueError()
        return int(m.group(1)), int(m.group(2)), int(m.group(3))
    return [extract(x) for x in instructions]

def part1(stacks: List[List[str]], instructions: List[Tuple[int, int, int]]) -> str:
    def apply(instruction: Tuple[int, int, int]) -> None:
        count, fr, to = instruction
        for i in range(count):
            stacks[to - 1].append(stacks[fr - 1].pop())
    for instruction in instructions:
        apply(instruction)
    return "".join(s[-1] for s in stacks)

def part2(stacks: List[List[str]], instructions: List[Tuple[int, int, int]]) -> str:
    def apply(instruction: Tuple[int, int, int]) -> None:
        count, fr, to = instruction
        moved = []
        for i in range(count):
            moved.append(stacks[fr - 1].pop())
        moved.reverse()
        stacks[to - 1].extend(moved)
    for instruction in instructions:
        apply(instruction)
    return "".join(s[-1] for s in stacks)

if __name__ == '__main__':
    lines = read_file('day05.txt')
    i = 0
    while lines[i].strip():
        i += 1
    stacks = parse_stacks(lines[:i - 1])
    instructions = parse_instructions(lines[i + 1:])

    print(part1([x[:] for x in stacks], instructions))
    print(part2(stacks, instructions))