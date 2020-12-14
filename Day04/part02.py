from pathlib import Path
import re
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


def search(item, lookup):
    if lookup in item:
        return True


def passport_has_reqd_keys(dict):
    if len(dict) == 8:
        valid = True
    elif len(dict) == 7 and 'cid' not in dict:
        valid = True
    else:
        valid = False
    return valid


HAIRCOLOR_PATTERN = re.compile(r"(\A#)[0-9a-f]{6}$")
eyecolor_list = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
PASSPORTID_PATTERN = re.compile(r"\d{9}$")
HEIGHT_PATTERN = re.compile(r"(\d+)(cm|in)")


def passport_values_are_valid(dict):
    if int(dict['byr']) < 1920 or int(dict['byr']) > 2002:
        valid = False
    elif int(dict['iyr']) < 2010 or int(dict['iyr']) > 2020:
        valid = False
    elif int(dict['eyr']) < 2020 or int(dict['eyr']) > 2030:
        valid = False
    elif not HEIGHT_PATTERN.match(dict['hgt']):
        valid = False
    elif not HAIRCOLOR_PATTERN.match(dict['hcl']):
        valid = False
    elif not any(n in dict['ecl'] for n in eyecolor_list):
        valid = False
    elif not PASSPORTID_PATTERN.match(dict['pid']):
        valid = False
    else:
        valid = True
    return valid


def hgt_is_valid(dict):
    if search(dict['hgt'], 'cm'):
        if int(dict['hgt'].replace('cm', '')) < 150 or int(dict['hgt'].replace('cm', '')) > 193:
            valid = False
        else:
            valid = True
    elif search(dict['hgt'], 'in'):
        if int(dict['hgt'].replace('in', '')) < 59 or int(dict['hgt'].replace('in', '')) > 76:
            valid = False
        else:
            valid = True
    else:
        valid = False
    return valid


def compute(input_str: str) -> int:
    finaldict = convert_to_dict(input_str)
    count = 0
    for passport in finaldict:
        if passport_has_reqd_keys(passport):
            if passport_values_are_valid(passport):
                if hgt_is_valid(passport):
                    count += 1
    return count


TEST_INPUTS = [
    ('''eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719''', 4)
]


@pytest.mark.parametrize("input_str,expected", TEST_INPUTS)
def test(input_str: str, expected: int) -> None:
    assert compute(input_str) == expected


def main() -> int:
    with INPUTS_FILE.open() as fp:
        return compute(fp.read())


if __name__ == "__main__":
    print(f"The answer is {main()}")
