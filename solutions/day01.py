
import heapq
from typing import List
from utils import read_file

def part1(lines: List[str]) -> int:
    result = 0
    cur = 0
    for line in lines:
        if line:
            cur += int(line)
        else:
            result = max(result, cur)
            cur = 0
    result = max(result, cur)
    return result

def part2(lines: List[str]) -> int:
    heap = []
    cur = 0
    for line in lines:
        if line:
            cur += int(line)
        else:
            heapq.heappush(heap, cur)
            cur = 0
    heapq.heappush(heap, cur)
    return sum(heapq.nlargest(3, heap))

if __name__ == '__main__':
    lines = [x.strip() for x in read_file("day01.txt")]
    print(part1(lines))
    print(part2(lines))