# Jacobus Burger (2024-12-01 started, 2024-12-23 completed)
# Advent Of Code - Day 1

# Day 1 - Parser
# Parsing seems to be a consistently different task between days so
#   I've opted to write the input parsing as a seperate function to
#   take the inputs with.
# The idea here is to split the two columns into two lists of int
#   into two lists `A` and `B`.
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
# My understanding is we take the difference between the left and right
#   elements of the lists after they're sorted. Then sum the difference.
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
# Solution Idea:
# A direct approach is to take the two lists, sort them, and add their
#   differences as explained above.
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
    # parse arrays
    A, B = parse(filename)
    # sort arrays
    A.sort()
    B.sort()
    # calculate sum of difference
    return sum([abs(a - b) for a, b in zip(A, B)])
# Thoughts:
# This is the most obvious solution. There's probably a better approach
#   by sorting inputs as they're received. But the program is only
#   roughly O(2n) at worst right now.


# Part 2 - Theory
# My understanding is we want the occurences in the right column of
#   each number from the left one, then multiply that coun with the
#   number we're seeking occurences for, and then add that to the total
#   and finally return a sum of it all.
# To do this, we can fallow the same parsing as part 1, but change
#   the logic for calculating.
# Example:
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3
#
# 3   3o
# 4   1o
# 2   0o
# 1   0o
# 3   3o
# 3   3o
# 9 + 4 + 0 + 0 + 9 + 9
# Solution Idea:
# The left column A will be left unsorted and the right column B will
#   be made into a hashmap storing the count of occurences of each
#   number in B.
# Method:
# 1. parse input into arrays A and B
# 2. create a hashmap of occurences from B
# 3. for each number in A, calculate the product of that number with its
#       occurences in B.
# Pseudocode:
#   1. parse
#   for a, b in read(file):
#       A.append(a)
#       B.append(b)
#   2. hashmap
#   map = {}
#   for value in B:
#       if value not in map:
#           map[value] = 1
#       else:
#           map[value] += 1
#   3. tally
#   return sum([a * map[a] for a in A])
# Notes:
# Part 2 of the pseudocode can be accomplished using Python's Counter
#   object from collections. I love snakelang 🐍
from collections import Counter

def part2(filename: str) -> int:
    # parse input
    A, B = parse(filename)
    # create hashmap
    map = Counter(B)  # I love snakelang 🐍
    # return total
    return sum([a * map[a] for a in A])
