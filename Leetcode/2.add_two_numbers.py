from typing import Optional
from Leetcode.leetcode import ListNode

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        ptr = dummy
        carry = 0

        while l1 or l2 or carry:

            s = carry

            if l1:
                s += l1.val
                l1 = l1.next

            if l2:
                s += l2.val
                l2 = l2.next

            carry = 1 if s // 10 else 0
            s = s % 10

            new = ListNode(s)

            ptr.next = new
            ptr = ptr.next

        return dummy.next