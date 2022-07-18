
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr != None and curr.next != None:
            if curr.next.val == curr.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head


list1 = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))


mySolution = Solution()
result = mySolution.deleteDuplicates(list1)

while result != None:
    print(result.val)
    result = result.next
