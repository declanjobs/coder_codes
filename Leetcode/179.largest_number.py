from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):

        def cmp(x, y):
            x = str(x)
            y = str(y)
            if x + y > y + x:
                return -1
            else:
                return 1

        nums = sorted(nums, key=cmp_to_key(cmp))
        largest_num = ''.join([str(x) for x in nums])

        return '0' if largest_num[0] == '0' else largest_num