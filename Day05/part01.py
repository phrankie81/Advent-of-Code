from pathlib import Path

import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def row_finder(str, range):
    FB = (range[1]-range[0]) // 2 + range[0]
    if str == 'F':
        range = [range[0], FB]
    else:
        range = [FB+1, range[1]]
    return range


def seat_finder(str, range):
    FB = (range[1]-range[0])  // 2 + range[0]
    if str == 'L':
        range = [range[0], FB]
    else:
        range = [FB+1, range[1]]
    return range


def compute(input_str: str) -> int:
    maxnumber = 1
    for line in input_str.split('\n'):
        myrange = [0, 127]
        seatrange = [0, 7]
        for str in line[0:7]:
            myrange = row_finder(str, myrange)
        row = myrange[1]

        for str in line[7:]:
            seatrange = seat_finder(str, seatrange)

        seat = seatrange[1]
        passport_id = row * 8 + seat
        if passport_id > maxnumber:
            maxnumber = passport_id
    return maxnumber



TEST_INPUTS = [
    ('''FBFBBFFRLR
BFFFBBFRRR
FFFBBBFRRR
BBFFBBFRLL''', 820)
]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")
