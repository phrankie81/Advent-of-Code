from pathlib import Path

import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def compute(input_str: str) -> int:
    new_list = input_str.split('\n')
    anotherlist = []
    for line in new_list:
        anotherline = line * 40
        anotherlist.append(anotherline)
    count = 0
    counter = 3
    for line in anotherlist[1:]:
        if line[counter] == '#':
            count += 1
        counter += 3
    return count


TEST_INPUTS = [
    ('''..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#''', 7)
]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")
