from lintcode import (
    ListNode,
)

class Solution:
    """
    @param head: a ListNode
    @param k: An integer
    @return: a ListNode
    """
    def reverse_k_group(self, head: ListNode, k: int) -> ListNode:
        # write your code here
        #self.print_list(head)

        dummy = ListNode(0, head)
        #dummy.next = head

        start = head
        end = self.next_seg(start, k)

        prev_end = dummy
        while start and end:
            #self.print_list(dummy.next)
            prev_end.next = self.reverse(start, end)

            # start and end swapped
            prev_end = start
            start = start.next
            end = self.next_seg(start, k)

        return dummy.next


    def next_seg(self, head, k):
        end = head
        for _ in range(k-1):
            if not end:
                break
            end = end.next

        return end


    """
    Reverse a segment of linked list, from head to tail
    Make sure the reversed list still in the master list
    Return the head of the reversed list
    """
    def reverse(self, head, tail) -> ListNode:

        #print(head.val, tail.val)
        #self.print_list(head)

        stop = tail.next
        curt = tail.next

        while head != stop:
            print(head.val)
            temp = head.next
            head.next = curt
            curt = head
            head = temp

        #self.print_list(curt)
        return curt

    def print_list(self, head):
        p = []

        while head:
            p.append(str(head.val))
            p.append('->')
            head= head.next

        p.append("None")

        print("".join(p))
