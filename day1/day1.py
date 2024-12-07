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
