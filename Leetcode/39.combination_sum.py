from typing import List


class Solution:

    def combinationSum(self, candidates: List[int], targets: int) -> List[List[int]]:

        ans = []

        def dfs(idx, current, target):

            if target == 0:
                ans.append(list(current))
                return

            if candidates[idx] <= target:
                current.append(candidates[idx])
                dfs(idx, current, target-candidates[idx])
                current.pop()

            if idx+1 < len(candidates):
                dfs(idx+1, current, target)

        dfs(0, [], targets)

        return ans

    def combinationSum(self, candidates: List[int], targets: int) -> List[List[int]]:

        ans = []

        def dfs(idx, current, target):

            if target == 0:
                ans.append(list(current))
                return

            for i in range(idx, len(candidates)):
                if candidates[i] <= target:
                    current.append(candidates[i])
                    dfs(i, current, target-candidates[i])
                    current.pop()

        dfs(0, [], targets)

        return ans