from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product_fwd = [0] * (len(nums) + 2)
        prefix_product_rev = [0] * (len(nums) + 2)

        nums = [1] + nums + [1]

        prev_sum_fwd = 1
        prev_sum_rev = 1
        for i in range(len(nums)):
            prefix_product_fwd[i] = prev_sum_fwd
            prev_sum_fwd *= nums[i]

            prefix_product_rev[len(nums)-1-i] = prev_sum_rev
            prev_sum_rev *= nums[len(nums)-1-i]

        for i in range(1, len(nums)):
            nums[i] = prefix_product_fwd[i] * prefix_product_rev[i]


        return nums[1:-1]