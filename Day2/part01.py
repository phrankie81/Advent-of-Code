from pathlib import Path
import re

import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def compute(input_str: str) -> int:
    # split_input = input_str.split("\n")
    new_list = [re.split(r'\s|-|: ', line) for line in input_str.split('\n')]
    counter = 0
    for line in new_list:
        min_num, max_num, charac, password = line
        count = password.count(charac)
        if (count >= int(min_num)) and (count <= int(max_num)):
            counter += 1
    return counter


TEST_INPUTS = [
    ("""1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc""", 2)
]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")
