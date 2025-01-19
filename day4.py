# Jacobus Burger (started 2025-01-18)
# 

# PART 1 - 
# So far the problem seems pretty simple. I need to implement a DFS that
#   starts on any X and goes in one of the 8 grid directions. If it finds
#   the letters "XMAS" in that order, then after fully exploring that X
#   mark it as done and move on to the next one. X's are chosen by simply
#   scanning across the grid.


# then utilize a modified DFS with a global list of explored roots (X's)
#   to explore and match every "XMAS" along the 8 grid directions
#   (which is vertical, horizontal, and diagonal)
def part1(filename: str) -> int:
    G = open(filename, "r").readlines()


# DFS for reference
# G is graph, v is starting vertex
# most straigh-forward solution
def dfs(G, v):
    visited, stack = [], [v]
    while stack:
        v = stack.pop()
        visited.append(v)
        for w in reversed(G[v]):
            if w not in visited:
                stack.append(w)
    return visited
