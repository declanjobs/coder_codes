from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        m = len(grid)
        if not m: return 0

        n = len(grid[0])

        fresh = 0
        time = 0
        rotten_q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten_q.append([i,j])

        directions = [[0,1], [1,0], [0,-1], [-1,0]]

        while rotten_q and fresh:

            for r in range(len(rotten_q)):
                ii, jj = rotten_q.popleft()

                for d in directions:

                    iii, jjj = ii + d[0], jj + d[1]

                    if not ((0<=iii<m and 0<=jjj<n) and grid[iii][jjj] == 1):
                        continue

                    grid[iii][jjj] = 2
                    rotten_q.append([iii,jjj])
                    fresh -= 1

            time += 1


        return time if fresh==0 else -1