from pathlib import Path
from verticalprint import print_vertical
INPUT_FILE = Path(__file__).parent / "input.txt"

with open(INPUT_FILE) as fp:
    input = fp.read().split('\n')

wherever = [line for line in input if 'shiny gold' in line]
print_vertical(wherever)
print()
def get_first_bag(line):
    first = line.split(',')
    return first[0].split(" bags")[0]


firstbags = [get_first_bag(line) for line in wherever]
print(firstbags)

for i in range(len(firstbags)):
    if firstbags[i] == 'shiny gold':
        del wherever[i]
firstbags.remove('shiny gold')

print_vertical(wherever)

for bag in firstbags:
    for line in input:
        if bag in line and line not in wherever:
            wherever.append(line)

print(len(wherever))
