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


# credit to user "Independent_Check_62" on https://www.reddit.com/r/adventofcode/comments/1h4ncyr/2024_day_2_solutions/
def valid(report: list) -> bool:
    # create a set of differences
    deltas = {report[i + 1] - report[i] for i in range(len(report) - 1)}
    # return true if it's a subset of the correct change and sign
    return deltas <= {1, 2, 3} or deltas <= {-1, -2, -3}


# PART 1 COMPLETE 2024-12-26, UPDATE 2025-01-10
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
# A slightly better approach simplified the problem by using set
#   membership as a filter for report validity.
def part1(filename: str) -> int:
    reports = parse(filename)
    total = sum([valid(report) for report in reports])
    return total



# PART 2 COMPLETE 2025-01-10
# Part 2 is part 1 but with a grace of one failure (bool flag)
# The solution to part 2 is to do the same as part 1 but to check the
#   combinations of the report with 1 level removed and if any of those
#   combinations are correct, to count it as safe and move on. Same as
#   before but hopefully it works properly this time!
def part2(filename: str) -> int:
    reports = parse(filename)
    total = sum([
        any(
            valid(report[:i] + report[i + 1:])
            for i in range(len(report))
        )
        for report in reports
    ])
    return total
