from typing import Optional
from Leetcode.leetcode import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode()
        dummy.next = head

        fast = dummy
        slow = dummy

        while n:
            fast = fast.next
            n -= 1


        while fast and fast.next:

            fast = fast.next
            slow = slow.next


        slow.next = slow.next.next

        return dummy.next