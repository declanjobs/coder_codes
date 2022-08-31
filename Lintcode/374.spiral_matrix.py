from typing import (
    List,
)

class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiral_order(self, matrix: List[List[int]]) -> List[int]:
        # write your code here

        m = len(matrix)
        if not m:
            return []

        n = len(matrix[0])

        directions = [[0,1], [1,0], [0, -1], [-1,0]]

        ans = []

        i,j = 0,0
        d = 0

        up_bond, left_bond = 0, 0
        down_bond, right_bond = m-1, n-1

        def is_valid(i,j):
            nonlocal matrix
            return up_bond <= i <= down_bond and left_bond <= j <= right_bond
            #and matrix[i][j] != float("inf")

        while is_valid(i,j):
            #print(i, j)

            ans.append(matrix[i][j])
            #matrix[i][j] = float("inf")

            ii, jj = i + directions[d][0], j + directions[d][1]

            if is_valid(ii,jj):
                i, j = ii, jj
            else:
                if d == 0:
                    up_bond += 1
                elif d == 1:
                    right_bond -= 1
                elif d == 2:
                    down_bond -= 1
                else:
                    left_bond += 1

                d += 1
                if d > 3:
                    d = 0
                i, j = i + directions[d][0], j + directions[d][1]

        return ans