# Jacobus Burger (started 2024-12-25)
# Day 2


# problem data comes as a list of rows with numbers (a list of number
#   lists). So it can be ingested and parsed one line at a time, each
#   line producing a list. I'll do that as a 2D list
def parse(filename: str) -> list[int]:
    with open(filename, "r") as file:
        # returns a 2D array of arrays of ints
        return [
            list(map(int, line.split()))
            for line in file.readlines()
        ]


# for part 1 it's helpful to be able to tell the sign of a difference
def sign(n: int) -> int:
    return (0 < n) - (0 > n)


# Part 1 checks if a report (line of input) is "safe" according to
#   the two requirements that for that level
# 1. all levels must be stricting increasing or decreasing in value
#   (must be monotonically ordered)
# 2. all adjacent levels must differ by >= 1 and <= 3
# 
# The most direct and simple solution is a sliding window to compare
#   levels that states a report as Unsafe if any of those conditions
#   fail to be met.
#   The number of safe reports is tallied, that sum is the solution.
