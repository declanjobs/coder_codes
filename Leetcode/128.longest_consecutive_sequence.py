from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)

        ans = 0

        for i in nums:

            if i - 1 not in hashset:
                ii = i

                while ii + 1 in hashset:
                    ii += 1

                #print(i, ii)
                if ii - i + 1 > ans:
                    ans = ii - i + 1
        return ans