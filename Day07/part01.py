from pathlib import Path
import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def compute(input_str: str) -> int:
    rules = []
    for _, line in enumerate(input_str.strip().split("\n")): #remove spaces and newline characters
        outer, b = line.replace("bags", "").replace("bag", "").split("contain") # break into outer bags and all inner bag. also remove the redundant words
        for c in b.replace(".", "").replace("no ", "0 no ").split(","): #iterate through inner bags and remove dots as well as make no = 0
            d = c.strip().split(" ")        # remove the space from ' 3 dark olive ' and split into three items
            rules.append((outer.strip(), " ".join(d[1:]), int(d[0]))) # append outer, inner bag color and number to rules

    leads_to_gold = {"shiny gold"} # create a set that contains everything to be counted. need to subtract 1 in final
    for outer, inner, n in rules * 10: # multiply rules by a large enough number so that loop will eventually go through all bags
        if inner in leads_to_gold: # if the inner bag is found in the set,
            leads_to_gold.add(outer) # then add the correspinding outer bag to it. by making it a set, there are no duplicates
    return len(leads_to_gold) - 1


TEST_INPUTS =[('''light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.''', 4)]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")