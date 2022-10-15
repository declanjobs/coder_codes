from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        from collections import defaultdict

        prefix_sum_lookup = defaultdict(int)
        prefix_sum_lookup[0] = 1
        prefix_sum = 0

        ans = 0
        for n in nums:

            prefix_sum += n

            if (prefix_sum - k) in prefix_sum_lookup:
                ans += prefix_sum_lookup[prefix_sum - k]

            prefix_sum_lookup[prefix_sum] += 1

        #print(prefix_sum_lookup)

        return ans