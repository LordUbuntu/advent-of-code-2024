# Jacobus Burger (2024-12-01)
# Advent Of Code - Day 1


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
# Solution Idea 1:
# From this, one direct idea is to take the two columns of numbers into their own
#   seperate lists, sort them, then take their sorted differences like above.
# Pseudocode 1:
#   input is array of string
#   A is array of int
#   B is array of int
#   total is int
#
#   for a, b in input:
#     add a to A
#     add b to B
#   sort A
#   sort B
#   for i in count(input):
#     total += abs(A[i] - B[i])
# Thoughts:
# This is the most obvious solution, though it's likely possible to use a
#   better approach by sorting inputs as they are received. It doesn't seem
#   possible to do better than two passes of n for O(2n) however, as the least
#   number may be at the end of either side of the list, and so it wouldn't
#   be possible to calculate the running differences without receiving the full
#   of both lists first. I considered a greedy approach to this, but that would
#   calculate the wrong differences preemptively. There is no way to preempt
#   the differences as far as I am aware.
