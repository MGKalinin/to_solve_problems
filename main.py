import collections
from typing import List

# Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 #острова
        q = collections.deque() #очередь с клетками
        visited = set()#посещённые клетки
        rows,cols = len(grid),len(grid[0])#количество строк,колонок


        def bfs(r,c):#bfs поиск в ширину
            direction = [[1,0],[-1,0],[0,1],[0,-1]]#направления шага по соседям
            while q:# пока очередь не пуста
                r,c = q.popleft()
                for i in range(len(direction)):
                    dr, dc = direction[i]
                    nr,nc = r + dr, c + dc
                    if (nr,nc) not in visited and 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
                        visited.add((nr,nc))
                        q.append((nr,nc))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    visited.add((row,col))
                    q.append((row,col))
                    bfs(row,col)
                    islands+=1
        return islands


grid = [
    ["0", "1", "1", "1", "0"],
    ["0", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution().numIslands(grid))