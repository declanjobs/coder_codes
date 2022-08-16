from collections import Counter

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def dfs(l):
            if l == n-1:
                res.append(list(nums))
                return
            for i in range(l, n):
                nums[l], nums[i] = nums[i], nums[l]   # swap nums[l] and nums[i]
                dfs(l+1)
                nums[l], nums[i] = nums[i], nums[l]  # swap them back

        dfs(0)

        return res

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results