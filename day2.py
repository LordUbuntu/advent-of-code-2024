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


# PART 1 COMPLETE 2024-12-26
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
def part1(filename: str) -> int:
    reports = parse(filename)
    # I could do this part with zips and maps, there's a method to pair adjacent elements in a list from my Lambdanomicon (Python Tricks Section) but I'll leave it as this explicit sliding window for now
    total = 0
    for report in reports:
        last_sign = sign(report[1] - report[0])  # start sign to compare
        for i in range(0, len(report) - 1):
            a, b = report[i], report[i + 1]
            if sign(b - a) != last_sign:
                break
            if abs(b - a) < 1 or abs(b - a) > 3:
                break
            last_sign = sign(b - a)
        else:
            # loop completed successfully, nothing unsafe
            total += 1
    return total



# Part 2 is part 1 but with a grace of one failure (bool flag)
# 
# My solution is to just copy-paste the code and add a "damper" flag
#   that will fail if the damper was already used.
# 
# Turns out the solution is more complicated than simply ignoring
#   a bad level greedily...
# A different solution might be to use a monotonic queue instead which
#   would "kick out" "bad" levels. I knew it was monotnically ordered
#   but I originally decided to skip writing one. In hindsight, a
#   monotonically ordered queue would make the first solution easy
#   (check if an element is rejected and return false) and also
#   make this one easy (allow one ejection and see if the solution
#   works by the same standard)
# I'm overcomplicating things. Brute force will work just fine here. I
#   can just go through index i across the list excluding that in the 
#   solution from part 1 meaning I just do 7 repeats of the same approach
def part2(filename: str) -> int:
    reports = parse(filename)
    total = 0
    for report in reports:
        last_sign = sign(report[1] - report[0])  # start sign to compare
        # need to figure out a way to iterate over every 1-level removed
        #   permutation of the report
        # maybe:
        # - make a copy
        # - remove an element (starting with none removed)
        # - iterate like in part 1 over the modified copy
        # - if it passes without failure, then count it
        report_counted = False
        for l in range(len(report) + 1):
            # make a modified report with a missing list
            if l > len(report) - 1:
                modified_report = report.copy()
            else:
                modified_report = report.copy()
                modified_report.pop(l)
            print(l, modified_report)
            # check if all remaining levels pass
            for i in range(0, len(modified_report) - 1):
                a, b = modified_report[i], modified_report[i + 1]
                print("  ", i, a, b)
                if sign(b - a) != last_sign:
                    break
                if abs(b - a) < 1 or abs(b - a) > 3:
                    break
                last_sign = sign(b - a)
            else:
                print("counted\n\n")
                total += 1
                report_counted = True
                break  # upon a success, count the report ONCE!
        if report_counted:
            continue
    return total
