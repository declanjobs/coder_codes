from typing import Optional
from Leetcode.leetcode import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy0 = ListNode()
        dummy1 = ListNode()
        dummy2 = ListNode()

        dummy0.next = dummy1
        dummy1.next = dummy2
        dummy2.next = head


        ptr0 = dummy0
        ptr1 = dummy1
        ptr2 = dummy2

        def node_swap(n_pre, n0, n1):

            n1_next = n1.next

            n_pre.next = n1
            n1.next = n0
            n0.next = n1_next

            # return the tail of the swapped segment
            return n0

        while ptr1 and ptr2:

            ptr2 = node_swap(ptr0, ptr1, ptr2)

            ptr0 = ptr2
            ptr1 = ptr2.next
            ptr2 = ptr1.next if ptr1 else None


        return dummy1.next