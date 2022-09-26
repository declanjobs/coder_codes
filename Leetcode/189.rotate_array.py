from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k %= len(nums)

        if k == 0:
            return

        cache = []
        from_cache = False

        for i in range(len(nums)):

            idx = (i + k) % len(nums)
            cache.append(nums[idx])

            if from_cache:
                temp = cache.pop(0)
            else:
                temp = nums[i]

            nums[idx] = temp

            if len(cache) == k:
                from_cache = True