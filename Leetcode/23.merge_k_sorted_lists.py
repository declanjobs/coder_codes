from typing import (
    List,
    Optional,
)

from Leetcode.leetcode import ListNode

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        from heapq import heappush, heappop

        heap = []

        for l in lists:
            if l:
                # put id(l) here as an unique indentifier as l.val can have dups
                heappush(heap, (l.val, id(l), l))


        dummy = ListNode()
        ptr = dummy

        while heap:
            _, _, l = heappop(heap)

            ptr.next = l
            ptr = ptr.next
            l = l.next

            if l:
                heappush(heap, (l.val, id(l), l))

        return dummy.next