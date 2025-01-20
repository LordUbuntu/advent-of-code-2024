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
    G = open(filename).read().splitlines()


from itertools import product, repeat
def count_matches(grid: list, root: tuple) -> int:
    count = 0
    # create a set of directions to explore around the root X
    directions = list(product(*repeat(range(-1, 2), 2)))
    directions.remove((0, 0))
    # go through each direction
    print(directions)
    for dx, dy in directions:
        string = []
        x = root[0]
        y = root[1]
        print("  ", dx, dy)
        # get the current string in one of the 8 directions
        for _ in range(4):
            # end if OOB
            if x < 0 or x >= len(grid[0]):
                break
            if y < 0 or y >= len(grid[0]):
                break
            print("   ", x, y, grid[y][x])
            # add current letter to string
            string.append(grid[y][x])
            # go to next step in sequence
            x += dx
            y += dy
        print("    ", string)
        # check if string is correct
        if ''.join(string) == "XMAS":
            count += 1
    return count
