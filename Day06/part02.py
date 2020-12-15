from pathlib import Path
import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def compute(input_str: str) -> int:
    data_list = input_str.split('\n\n')
    groups = [line.split() for line in data_list]
    number = []
    for group in groups:
        count = len(set.intersection(*(set(s) for s in group)))
        number.append(count)
    return sum(number)


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

b''', 6)]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")