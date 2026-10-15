import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #задать начальное количество островов
        islands = 0
        #вычислить количество строк, столбцов
        rows, cols = len(grid),len(grid[0])
        #инициализировать множество посещённых клеток
        visited =set()
        #реализовать bfs итеративный алгоритм
        def bfs(r,c):
            q = collections.deque()#очередь
            visited.add((r,c))# добавить ячейку в посещённеы
            q.append((r,c))# добавить в очередь
            while q:# пока очередь не пуста
                r,c = q.popleft()
                direction = [[1,0],[-1,0],[0,1],[0,-1]]# есть четыре направления вправо +1 0 влево -1 0 вниз 0 -1  вверх 0 +1
                for dr,dc in direction:# для направления+строка ,направления +столбец
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]=="1" and (nr,nc) not in visited: # если они находятся в пределах строи ,пределах столбца
        #     и ячейка куда шагнули ==1
                        # и позиция не посещена
                        q.append((nr,nc))# то добавить её в очередь
                        visited.add((nr,nc))#  добавить эту позицию в посещённые

        # пройти по строкам
        # проитй по столбцам
        # если яцейка 1 и мы её не посещали
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]=="1" and (row, col) not in visited:
                    bfs(row,col) #bfs
                    islands += 1 #увеличить количество островов
        return islands #вернуть количество островов

grid = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]
# Output: 4
print(Solution().numIslands(grid))
