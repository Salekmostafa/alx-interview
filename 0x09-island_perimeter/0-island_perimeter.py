def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.
    :param grid: List[List[int]], a grid of integers where 0 represents water and 1 represents land.
    :return: int, the perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check for adjacent land cells to subtract shared edges
                if row > 0 and

