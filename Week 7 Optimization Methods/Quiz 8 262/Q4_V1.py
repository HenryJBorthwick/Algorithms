"""A program to read a grid of weights from a file and compute the 
   minimum cost of a path from the top row to the bottom row
   with the constraint that each step in the path must be directly
   or diagonally downwards. 
   This question has a large(ish) 200 x 200 grid and you are required
   to use a bottom-up DP approach to solve it.
"""
INFINITY = float('inf')  

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
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    # Create a 2D cost table with the same dimensions as the grid
    cost_table = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    
    # Initialize the cost table's first row with the grid's first row values
    cost_table[0] = list(grid[0])

    # Fill the cost table
    for row in range(1, n_rows):
        for col in range(n_cols):
            # The cost is the cell's own value plus the minimum cost of the 
            # neighboring cells in the previous row.
            cost_table[row][col] = grid[row][col] + min(cost_table[row - 1][max(0, col - 1): min(n_cols, col + 2)])
    
    # The total minimum cost is the minimum cost among all cells in the last row.
    best = min(cost_table[-1])
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