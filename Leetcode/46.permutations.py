from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []

        def dfs(current, numbers):

            if len(numbers) == 0:
                ans.append(list(current))
                return


            for _ in range(len(numbers)):

                current.append(numbers.pop(0))

                dfs(current, numbers)

                numbers.append(current.pop())


        dfs([], nums)

        return ans


