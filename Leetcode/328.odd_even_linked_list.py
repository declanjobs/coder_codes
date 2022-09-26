from typing import Optional
from Leetcode.leetcode import ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyEven = ListNode(2)
        dummyOdd  = ListNode(1)

        dummyOdd.next = head

        pre_ptr = dummyOdd
        ptr = head
        odd_ptr = dummyEven

        idx = 1
        while ptr:

            if idx % 2 == 0:

                pre_ptr.next = ptr.next
                odd_ptr.next = ptr

                ptr = ptr.next

                odd_ptr = odd_ptr.next
                odd_ptr.next = None

            else:

                pre_ptr = ptr
                ptr = ptr.next

            idx += 1

        pre_ptr.next = dummyEven.next

        return dummyOdd.next
