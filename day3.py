# Jacobus Burger (started 2025-01-11)
# Day 3
import re


# first part is parsing, pattern as input incase that's changed
def parse(filename: str, pattern: str) -> list:
    return re.findall(pattern, open(filename, "r").read())


# PART 1 - COMPLETED 2025-01-13
# day 3 part 1 is simple, just use regex to match specified pattern,
#   then calculate it
def part1(filename: str) -> int:
    # mul\(\d{1,3}\,\d{1,3}\) == mul(123,456)
    expr = r"mul\(\d{1,3}\,\d{1,3}\)"
    operations = parse(filename, expr)
    # get the pair of numbers of each operation, then sum their products
    return sum([    # return sum of
        n[0] * n[1] # the products of
        for n in [  # each pair of numbers a,b from inputs "mul(a,b)"
            list(map(int, operation.strip("mul()").split(',')))
            for operation in operations
        ]
    ])


# PART 2 -
# day 3 part 2 is abot as simple. The difference is that the regex to
#   match with this time needs to match between tokens "do()" up until
#   "don't()"
def part2(filename: str) -> int:
    # match all the the substrings between "do()" and "don't()"
    regex = r"(?:do\(\)|^)(.*?)(?:don\'t\(\)|$)"
    matches = re.findall(regex, open(filename, "r").read())
    # match all mul operations within those substrings
    str = ''.join(matches)
    print(str)
    regex = r"mul\(\d{1,3}\,\d{1,3}\)"
    operations = re.findall(regex, str)
    print(operations)
    # return the sum like before
    return sum([    # return sum of
        n[0] * n[1] # the products of
        for n in [  # each pair of numbers a,b from inputs "mul(a,b)"
            list(map(int, operation.strip("mul()").split(',')))
            for operation in operations
        ]
    ])
