import collections
from typing import List

#Flood Fill

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = collections.deque()
        sample = image[sr][sc]#образец для сравнения
        directions = [[1,0],[-1,0],[0,-1],[0,1]]#направления движения
        q.append((sr,sc))#добавили в очередь
        visited = set()
        visited.add((sr,sc))#добавили в посещённые
        rows, cols = len(image), len(image[0])
        image[sr][sc] = color#перекрасиил в новый цвет

        while q:
            (sr,sc) = q.popleft()
            for dr,dc in directions:
                nr,nc = sr + dr, sc + dc
                if 0<=nr<rows and 0<=nc<cols and (nr,nc) not in visited and image[nr][nc] == sample:
                    q.append((nr,nc))
                    visited.add((nr,nc))
                    image[nr][nc] = color#надо закрасить после совпадения и посещения
        return image



image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

# Output: [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
print(Solution().floodFill(image,sr,sc,color))
