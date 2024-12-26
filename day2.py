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
