# Jacobus Burger (2024-12-01)
# Advent Of Code - Day 1

# Day 1 - Parser
# From my understanding, the parsing from part 1 (and parsing for any day) is
#   the same between parts, and sometimes between days too. So it makes the
#   most sense to write the parse seperate of each part's solver.
def parse(filename: str) -> list:
    A, B = [], []
    # read file by line (input)
    with open(filename, "r") as file:
        # == parse input ==
        for line in file.readlines():
            # get int a and b from col A and B
            a, b = map(int, line.split())
            # put into respective arrays
            A.append(a)
            B.append(b)
    return [A, B]


# Part 1 - Theory
# My understanding is we want to take the difference between the left and right
#   elements of the list once both sides are sorted. Thus we tally the
#   difference between each list
# Example:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
#
# 1   3   d2
# 2   3   d1
# 3   3   d0
# 3   4   d1
# 3   5   d2
# 4   9   d5
# 2 + 1 + 0 + 1 + 2 + 5 = 11
#
# Solution Idea:
# From this, one direct idea is to take the two columns of numbers into their own
#   seperate lists, sort them, then take their sorted differences like above.
# Method:
#   1. parse input into arrays A and B
#   2. sort A and B
#   3. calculate sum of differences
# Pseudocode:
#   1. parse
#   for a, b in read(file):
#       A.append(a)
#       B.append(b)
#   2. sort
#   A.sort()
#   B.sort()
#   3. calculate (solve)
#   return sum([abs(a - b) for a, b in zip(A, B)])
def part1(filename: str) -> int:
        A, B = parse(filename)
        # == solve ==
        # sort arrays
        A.sort()
        B.sort()
        # calculate sum of difference
        total = sum([abs(a - b) for a, b in zip(A, B)])
        # same as doing:
        # total = 0
        # for i in range(len(A)):
        #     total += abs(A[i] - B[i])
        return total
# Thoughts:
# This is the most obvious solution, though it's likely possible to use a
#   better approach by sorting inputs as they are received. It doesn't seem
#   possible to do better than two passes of n for O(2n) however, as the least
#   number may be at the end of either side of the list, and so it wouldn't
#   be possible to calculate the running differences without receiving the full
#   of both lists first. I considered a greedy approach to this, but that would
#   calculate the wrong differences preemptively. There is no way to preempt
#   the differences as far as I am aware.
# One potential improvement is to use a sort of selection sort or dequeue to
#   add elements in a sorted order as they are received, so that the sort step
#   is unnecessary later. It's unclear if that has any performance improvement
#   though...


# Part 2 - Theory
# TODO
