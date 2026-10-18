import collections
from typing import List

#Number of Islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            q.append((r,c))
            visited.add((r,c))
            while q:
                r, c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r + dr, c + dc
                    if 0<=nr<rows and  0<=nc<cols and  grid[nr][nc] == "1" and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    islands += 1
        return islands

grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
print(Solution().numIslands(grid))
