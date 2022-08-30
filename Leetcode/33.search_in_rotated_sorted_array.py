class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1

        while left < right - 1:

            mid = (left + right) // 2

            #print(left, mid, right)

            if nums[left] <= target <= nums[mid] or \
                target <= nums[mid] <= nums[right] or  \
                nums[mid] <= nums[right] <= nums[left] <= target:
                right = mid
            else:
                left = mid

        #print(left, right)

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        else:
            return -1