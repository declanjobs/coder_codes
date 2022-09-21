from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        # write your code here

        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])

        directions = [[-1,0], [1,0], [0,-1], [0,1]]

        pacific_entry = [[0, i] for i in range(n)] + [[j, 0] for j in range(1, m)]
        atlantic_entry = [[m-1, i] for i in range(n)] + [[j, n-1] for j in range(m-1)]

        #print(pacific_entry)
        #print(atlantic_entry)

        def dfs(point, hist):
            i, j = point[0], point[1]

            if (i, j) in hist:
                return
            hist.add((i, j))

            for d in directions:
                ii, jj = i + d[0], j + d[1]

                if 0 <= ii < m and 0 <= jj < n:

                    if matrix[ii][jj] >= matrix[i][j]:
                        dfs([ii,jj], hist)

        pacific_hist = set()
        atlantic_hist = set()
        for p in pacific_entry:
            dfs(p, pacific_hist)

        for p in atlantic_entry:
            dfs(p, atlantic_hist)

        #print(pacific_hist)
        #print(atlantic_hist)

        ans = []
        for p in pacific_hist:
            if p in atlantic_hist:
                ans.append(p)

        #print(ans)

        return ans

    # This also works but too slow, dfs on all nodes, whereas the previous solution
    # only dfs on perimeter nodes
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        if not m: return []
        n = len(heights[0])

        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        ans = []


        def dfs(x, y):

            pac, atl = False, False

            if x == 0 or y == 0:
                pac = True

            if x == m-1 or y == n-1:
                atl = True

            if pac and atl:
                return pac, atl

            pac_, atl_ = False, False

            for d in directions:

                xx, yy = x + d[0], y + d[1]

                if 0 <= xx < m and 0 <= yy < n and (xx, yy) not in visited:

                    if heights[xx][yy] <= heights[x][y]:

                        visited.add((xx, yy))

                        pac_, atl_ = dfs(xx, yy)

                        pac |= pac_
                        atl |= atl_

                        if pac and atl: break

            return pac, atl


        for i in range(m):
            for j in range(n):
                visited = set()
                pac, atl = dfs(i, j)

                if pac and atl:
                    ans.append([i, j])

        return ans
