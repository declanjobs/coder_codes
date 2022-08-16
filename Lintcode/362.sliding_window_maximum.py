from typing import (
    List,
)

from collections import deque
from heapq import heappush, heappop

# Aug, 2022, Rivian interview question

class Solution:
    """
    @param nums: A list of integers.
    @param k: An integer
    @return: The maximum number inside the window at each moving.
    """
    """
        Stack Implementation. This is faster than HEAP
    """
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        # write your code here

        # Keep q in descending order ***
        # [idx, x]
        q = deque([])

        ans = []

        for idx, x in enumerate(nums):
            #print(q)

            if q and (len(q) == k or q[0][0] == idx-(k)):
                q.popleft()

            while q and q[-1][1] <= x:
                q.pop()

            q.append([idx, x])

            if q and idx >= k-1:
                ans.append(q[0][1])

        return ans


    """
        Heap Implementation
    """
    def max_sliding_window(self, nums: List[int], k: int) -> List[int]:
        # write your code here


        # Make it a Max Heap
        # [x, idx]
        heap = []
        ans = []

        for idx, x in enumerate(nums):
            #print(heap)

            # Pop the min value that is out of the window
            while heap and (heap[0][1]) <= idx-(k):
                heappop(heap)

            # Negate the value makes it a max heap
            heappush(heap, [x*-1, idx])
            #print(heap)

            if heap and idx >= k-1:
                ans.append(heap[0][0]*-1)

        return ans