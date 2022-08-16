class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = 0

        #print(nums)
        _num = [0 for _ in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            _num[i] = nums[i-1] + _num[i-1]

        #nums = [0] + nums
        #print(nums)
        for i in range(len(_num)):

            for j in range(i+1, len(_num)):

                if (_num[j] - _num[i]) == k:
                    #print(i,j)
                    ans += 1



        return ans