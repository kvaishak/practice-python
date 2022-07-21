# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# https://leetcode.com/problems/reverse-linked-list/


from hashlib import new
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()

        while head != None:
            currEle = head
            head = head.next

            currEle.next = newList.next
            newList.next = currEle

        return newList.next


list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))


mySolution = Solution()
print(mySolution.reverseList(list1))
