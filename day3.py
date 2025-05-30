# Jacobus Burger (started 2025-01-11)
# Day 3
import re


# first part is parsing, pattern as input incase that's changed
def parse(filename: str, pattern: str) -> list:
    return re.findall(pattern, open(filename, "r").read())


# PART 1 - COMPLETED 2025-01-13
# The first part is simple. Utilize a regex to match the specified
#   substring of the form "mul(abc,def)", then calculate those
#   products, and add to the sum
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


# PART 2 - COMPLETED 2025-01-18
# This one was great becaue I learned a ton about regex along the way
# I initially thought to try creating a regex to only capture substrings
#   between "do()" and "don't()" but after checking solutions once my
#   3 day max limit was up, I decided to go with my original idea of
#   going iteratively and switching between ignoring and accepting "mul"
#   commands using a flag
def part2(filename: str) -> int:
    total = 0
    regex = r"do\(\)|don\'t\(\)|mul\(\d{1,3},\d{1,3}\)"
    string = open(filename, "r").read()
    do = True
    for substring in re.finditer(regex, string):
        match substring[0]:
            case "do()":
                do = True
            case "don't()":
                do = False
            case _:
                if do:
                    nums = [
                        int(num)
                        for num in substring[0].strip("mul()").split(',')
                    ]
                    total += nums[0] * nums[1]
    return total
