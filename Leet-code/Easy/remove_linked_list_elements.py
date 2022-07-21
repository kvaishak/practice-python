# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.


# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
# https://leetcode.com/problems/remove-linked-list-elements/

from os import remove
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        while curr != None:
            if curr == head and curr.val == val:
                head = curr.next
                curr = curr.next
            elif curr.next and curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head

        # Recursive Solution : FASTER AND TAKES MORE SPACE THAN THE PREVIOUS IMPLEMENTATION
        # if head == None:
        #     return None
        # if head.val == val:
        #     return self.removeElements(head.next, val)
        # head.next = self.removeElements(head.next, val)
        # return head


l1 = ListNode(1)

l2 = ListNode(2)
l1.next = l2

l3 = ListNode(6)
l2.next = l3

l4 = ListNode(3)
l3.next = l4

l5 = ListNode(4)
l4.next = l5

l6 = ListNode(5)
l5.next = l6

l7 = ListNode(6)
l6.next = l7

l7.next = None


mySolution = Solution()
print(mySolution.removeElements(l1, 6))
