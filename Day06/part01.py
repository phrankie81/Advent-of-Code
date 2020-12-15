from pathlib import Path
from collections import Counter
import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def compute(input_str: str) -> int:
    data_list = input_str.split('\n\n')
    groups = []
    for line in data_list:
        gr = "".join(line.split("\n"))
        groups.append(gr)

    counts = []
    for i in groups:
        number = Counter(i)
        counts.append(len(number))
    return sum(counts)


TEST_INPUTS =[('''abc

a
b
c

ab
ac

a
a
a
a

b''', 11)]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")