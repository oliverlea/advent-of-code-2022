
from typing import List, Tuple

Loc = Tuple[int, int]

def read_file(fn: str) -> List[str]:
    with open('./input/' + fn, 'r') as f:
        return f.readlines()