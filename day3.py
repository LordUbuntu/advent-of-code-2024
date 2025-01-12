# Jacobus Burger (started 2025-01-11)
# Day 3
import re


# first part is parsing, pattern as input incase that's changed
def parse(filename: str, pattern: str) -> list:
    return re.findall(pattern, open(filename, "r").read())

# mul\(\d{1,3}\,\d{1,3}\)


# day 3 part 1 is simple, just use regex to match specified pattern,
#   then calculate it
