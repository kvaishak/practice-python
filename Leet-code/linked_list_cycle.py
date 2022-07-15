
# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.


# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Floyds Cycle Detection Algorithm
        turtle = head
        hare = head

        while hare != None and hare.next != None:
            turtle = turtle.next
            hare = hare.next.next
            if turtle == hare:
                return True

        return False


l1 = ListNode(-1)

l2 = ListNode(-7)
l1.next = l2

l3 = ListNode(7)
l2.next = l3

l4 = ListNode(-4)
l3.next = l4

l4.next = l1

# l5 = ListNode(19)
# l4.next = l5

# l6 = ListNode(6)
# l5.next = l6

# l7 = ListNode(-9)
# l6.next = l7

# l8 = ListNode(-5)
# l7.next = l8

# l9 = ListNode(-2)
# l8.next = l9

# l10 = ListNode(-5)
# l9.next = l10

# l10.next = l10


mySolution = Solution()
print(mySolution.hasCycle(l1))
