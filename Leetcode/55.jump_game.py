from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_idx = 0

        idx = 0
        while idx < len(nums) and idx <= max_idx:
            max_idx = max(max_idx, idx + nums[idx])
            idx += 1

        return max_idx >= len(nums) - 1