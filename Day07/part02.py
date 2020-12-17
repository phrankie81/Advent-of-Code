import pprint
import re
import collections
from pathlib import Path
from typing import Set, Dict, List, Tuple

INPUTS_FILE = Path(__file__).parent / "input.txt"


with INPUTS_FILE.open() as fp:
    INPUT_S = fp.read()

# INPUT_S = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.'''

LINE_RE = re.compile(r'^(\w+ \w+) bags contain (.+)$')
CHILD_RE = re.compile(r'(\d+) (\w+ \w+)')

parents = collections.defaultdict(list)
for line in INPUT_S.splitlines():
    line_match = LINE_RE.match(line)
    assert line_match, line
    parent = line_match[1]
    rest = line_match[2]
    # print(line_match[1])

    for num, child in CHILD_RE.findall(rest):
        parents[child].append(parent)


def parse_part2() -> Dict[str, List[Tuple[int, str]]]:
    bags = collections.defaultdict(list)
    for line in INPUT_S.splitlines():
        line_match = LINE_RE.match(line)
        assert line_match, line
        parent = line_match[1]
        rest = line_match[2]

        children = [(int(n), child) for n, child in CHILD_RE.findall(rest)]
        bags[parent] = children
    return bags


# part 1
def compute(color: str) -> Set[str]:
    ret = {color}
    for item in parents[color]:
        ret |= compute(item)
    return ret


# print(parents)
print(f"part 1 answer = {len(compute('shiny gold')) -1}")


# part 2
colorbags = parse_part2()


def computepart2(n, color) -> int:
    ret = n
    for child_number, child in colorbags[color]:
        ret += computepart2(n * child_number, child)
    return ret


print(f'part 2 answer = {computepart2(1, "shiny gold")-1}')
