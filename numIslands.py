############ Method 1: Using BFS##############
"""
Time Complexity: O(M * N)
Space complexity: O(M+N)
"""
from queue import Queue
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: if the grid is None or empty, return 0 as there are no islands.
        if grid is None or len(grid) == 0:
            return 0
        
        count = 0  # Initialize the count of islands.
        q = Queue()  # Queue to perform BFS.

        # Define the four possible directions to move in the matrix (Up, Down, Left, Right).
        Dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Traverse through each cell in the grid.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If a cell contains '1', it's the start of a new island.
                if grid[i][j] == '1':
                    count += 1  # Increment island count.
                    q.put([i, j])  # Add the cell to the BFS queue.
                    grid[i][j] = '2'  # Mark the cell as visited by changing it to '2'.

                    # Perform BFS to mark all cells in this island.
                    while not q.empty():
                        curr = q.get()
                        for d in Dirs:
                            nr = curr[0] + d[0]  # Calculate the new row index.
                            nc = curr[1] + d[1]  # Calculate the new column index.
                            # Check if the new cell is within bounds and contains '1'.
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == '1':
                                grid[nr][nc] = '2'  # Mark the new cell as visited.
                                q.put([nr, nc])  # Add the new cell to the queue.
        
        # Return the total number of islands found.
        return count



############### Method 2: Using DFS##############


"""
Time Complexity: O(M * N)
Space complexity: O(M * N)
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: if the grid is None or empty, return 0 as there are no islands.
        if grid is None or len(grid) == 0:
            return 0
        
        count = 0
        self.Dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Directions for exploring neighbors
        
        # Traverse through the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an unvisited part of an island
                    count += 1  # Increment the island count
                    self.dfs(grid, i, j)  # Use DFS to mark the entire island
        
        return count  # Return the total number of islands
    
    def dfs(self, grid: List[List[str]], row: int, col: int):
        # Base Case: If out of bounds or at a cell that is not part of an island, return.
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '1':
            return
        
        # Mark the current cell as visited by changing '1' to '2'
        grid[row][col] = '2'
        
        # Explore all four possible directions (up, down, left, right)
        for d in self.Dirs:
            nr = row + d[0]
            nc = col + d[1]
            self.dfs(grid, nr, nc)  # Recursively call DFS for each neighbor



