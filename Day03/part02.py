from pathlib import Path
import math
import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def compute(input_str: str) -> int:
    tuple_list = [[1,1], [3,1], [5,1], [7,1], [1,2]]
    new_list = input_str.split('\n')
    anotherlist = []
    for line in new_list:
        anotherlist.append(line*80)
    lenlist = len(anotherlist)
    results = []
    for pair in tuple_list:
        count = 0
        counter = pair[0]
        for line in anotherlist[pair[1]:lenlist:pair[1]]:
            if line[counter] == '#':
                count += 1
            counter += pair[0]
        results.append(count)
    return math.prod(results)


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
.#..#...#.#''', 336)
]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")
