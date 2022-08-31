from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left, right = 0, len(nums) - 1

        i = 0

        def swap(l, idx_1, idx_2):
            l[idx_1], l[idx_2] = l[idx_2], l[idx_1]

        while left < right and i <= right:

            if nums[i] == 0:
                swap(nums, i, left)
                left += 1
                i+=1
            elif nums[i] == 2:

                swap(nums, i, right)
                right -= 1
            else:
                i += 1