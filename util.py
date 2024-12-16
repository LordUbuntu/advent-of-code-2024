# Jacobus Burger (2024-12-01)
# Common utilities for solving problems, including downloading
#   inputs, problem descriptions, and uploading solutions.
#
# Remember: premature optimization is the root of many coding evils
from typing import Iterator


# best way is to learn from the best, here's some references to look at
# - https://github.com/nitekat1124/advent-of-code-2024/blob/main/utils/files.py
# - https://github.com/NadiaMit/AdventOfCode2024/blob/main/helpers/helpers.py
# - https://github.com/nitekat1124/advent-of-code-2024


# A recurring pattern is to read one line at a time, so a generator
#   is a convenient pattern for parsing inputs
def by_line(filename: str) -> Iterator[str]:
    with open(filename, 'r') as file:
        for line in file.readlines():
            yield line
