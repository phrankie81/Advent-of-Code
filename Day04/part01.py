from pathlib import Path

import pytest

INPUTS_FILE = Path(__file__).parent / "input.txt"


def convert_to_dict(inputstr):
    first_breakdown = inputstr.split("\n\n")
    second_breakdown = []
    for string in first_breakdown:
        removespaces = ", ".join(string.split(" "))
        removenewline = ", ".join(removespaces.split("\n"))
        second_breakdown.append(removenewline)
    finaldict = []
    for test_str in second_breakdown:
        res = dict(map(str.strip, sub.split(':', 1)) for sub in test_str.split(', ') if ':' in sub)
        finaldict.append(res)
    return finaldict


def compute(input_str: str) -> int:
    finaldict = convert_to_dict(input_str)
    count = 0
    for passport in finaldict:
        if len(passport) == 8:
            valid = True
        elif len(passport) == 7 and 'cid' not in passport:
            valid = True
        else:
            valid = False
        if valid:
            count += 1
    return count


TEST_INPUTS = [
    ('''ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in''', 2)
]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")
