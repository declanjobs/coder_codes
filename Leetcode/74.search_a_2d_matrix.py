from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if not m:
            return False
        n = len(matrix[0])

        #print(m,n)

        def get_elm(idx):
            nonlocal m, n

            v_m = idx // n
            v_n = idx % n

            return matrix[v_m][v_n]

        l = m * n
        left, right = 0, l-1

        while left < right:

            mid = (left + right) // 2
            mid_val = get_elm(mid)

            if mid_val == target:
                return True
            elif mid_val > target:
                right = mid - 1
            else:
                left = mid + 1

        #print(left, right, mid)
        if get_elm(left) == target or get_elm(right) == target:
            return True

        return False



