from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtrack(current, left, right):

            if len(current) == 2 * n:
                ans.append("".join(current))
                return

            if left < n:
                current.append("(")
                backtrack(current, left+1, right)
                current.pop()


            if right < left:
                current.append(")")
                backtrack(current, left, right+1)
                current.pop()

        backtrack([], 0, 0)

        return ans