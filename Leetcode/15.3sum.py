from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            left , right = i+1, len(nums)-1
            while left < right:

                threeSums = nums[i] + nums[left] + nums[right]

                if threeSums == 0:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1

                elif threeSums > 0:
                    right -= 1
                else:
                    left += 1

        return ans