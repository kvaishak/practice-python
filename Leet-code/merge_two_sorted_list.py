# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
from hashlib import new
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newNode = ListNode()
        head = newNode

        while list1 != None and list2 != None:
            if list1.val >= list2.val:
                newNode.next = list2
                list2 = list2.next
            else:
                newNode.next = list1
                list1 = list1.next

            newNode = newNode.next

        newNode.next = list1 or list2
        return head.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))

mySolution = Solution()
print(mySolution.mergeTwoLists(list1, list2))
