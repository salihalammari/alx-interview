To solve the problem of calculating the perimeter of an island represented by a 2D grid where 1s represent land and 0s represent water, we can follow a systematic approach:

## Approach:

### 1. Iterate through the grid: Traverse each cell in the grid to identify land cells (cells with the value 1).

### 2. Calculate perimeter for each land cell:

 . Each land cell potentially contributes up to 4 sides to the perimeter.
 . Check the adjacent cells (up, down, left, right) to determine how many sides are exposed to water (0s).
 . If an adjacent cell is out of bounds (i.e., beyond grid boundaries) or contains water, it contributes to the perimeter.

### 3. Sum up the contributions: Accumulate the count of perimeter contributions from all land cells to get the total perimeter of the island.

## Implementation Details:

 . Use nested loops to iterate through each cell of the grid.
 . For each land cell (grid[i][j] == 1), check its four neighbors to determine if each neighbor contributes to the perimeter.
 . Handle edge cases such as cells on the boundary of the grid where neighbors might not exist.

Here is the Python function island_perimeter(grid) that implements the above approach:

```python
def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 possible directions (up, down, left, right)
                # If out of bounds or on water, add to perimeter
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1  # Top
                if i == rows - 1 or grid[i+1][j] == 0:
                    perimeter += 1  # Bottom
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1  # Left
                if j == cols - 1 or grid[i][j+1] == 0:
                    perimeter += 1  # Right
    
    return perimeter
```

## Explanation:

 . Initialization: Start with perimeter = 0 to accumulate the total perimeter. 
 . Nested Loops: Iterate through each cell (i, j) in the grid.
 . Conditionals: For each land cell (i, j), check its four adjacent cells. Each condition (if) checks if the adjacent cell is water (0) or if the current cell is on the boundary of the grid.
 . Perimeter Calculation: Increment perimeter whenever an adjacent cell is water or out of bounds.

## Edge Cases Considered:

 . Grid boundaries: Ensure checks for cells on the edge of the grid don't access out-of-bounds indices.
 . Grid size: The function handles grids up to 100x100 as specified.

## Conclusion:

 This function efficiently calculates the perimeter of the island by leveraging simple conditional logic and iteration over the grid. It meets all the requirements specified in the problem statement, including handling the grid completely surrounded by water and having only one contiguous island.
