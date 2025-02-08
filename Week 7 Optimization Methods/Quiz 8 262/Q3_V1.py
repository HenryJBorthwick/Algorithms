"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')  # Same as math.inf

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """
    Function to compute the minimum cost to reach from the top row to the bottom row
    in a given grid of integer weights.
    """

    # The number of rows in the grid
    n_rows = len(grid)

    # The number of columns in the grid
    n_cols = len(grid[0])

    # A dictionary to store previously computed cell costs.
    # This is what makes our function efficient for large inputs.
    memo = {}

    def cell_cost(row, col):
        """
        Helper function to compute the cost of getting to a given cell in the grid.
        We define it inside grid_cost so it has access to the 'memo' dictionary.
        """

        # If the cell is off the grid, its cost is infinite (we can't reach it).
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY

        # If we have already computed the cost of this cell, return it.
        elif (row, col) in memo:
            return memo[(row, col)]

        # If we haven't computed the cost of this cell yet, we do it now.
        else:
            # The cost is the cell's own value...
            cost = grid[row][col]

            # ...plus the minimum cost of the neighboring cells in the previous row, if we're not in the first row.
            if row != 0:
                cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, +2))

            # Save the computed cost in our 'memo' dictionary and return it.
            memo[(row, col)] = cost
            return cost
            
    # The total minimum cost is the minimum cost among all cells in the last row.
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best


    
    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return grid_cost(read_grid(filename))


# Test
print(file_cost('checkerboard.small.in')) #  Ouput 8

# Test
print(file_cost('checkerboard.medium.in')) #  

