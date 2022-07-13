
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Algorithm using O(n) space
        curr = head
        seen = {}

        while curr:
            if curr in seen:
                return seen[curr]
            seen[curr] = curr
            curr = curr.next

        return None

        # Floyd's Cycle Detection Algorithm (or) The Tortoise and the Hare Algorithm
        # NOT WORKING AS OF NOW

        # def isLoop (head: Optional[ListNode]) -> Optional[ListNode]:
        #     tortoise = head
        #     hare = head

        #     while hare != None and hare.next != None:
        #         tortoise = tortoise.next
        #         hare = hare.next.next

        #         if tortoise == hare:
        #             return tortoise

        #     return None

        # def startingNode (head: Optional[ListNode], matchNode: Optional[ListNode]) -> Optional[ListNode]:
        #     tempHead = head
        #     while tempHead != matchNode:
        #         head = head.next
        #         matchNode = matchNode.next
        #     return matchNode

        # matchNode = isLoop(head)
        # return startingNode(head, matchNode)


list1head = ListNode(-1)

l2 = ListNode(-7)
list1head.next = l2

l3 = ListNode(7)
l2.next = l3

l4 = ListNode(-4)
l3.next = l4

l5 = ListNode(19)
l4.next = l5

l6 = ListNode(6)
l5.next = l6

l7 = ListNode(-9)
l6.next = l7

l8 = ListNode(-5)
l7.next = l8

l9 = ListNode(-2)
l8.next = l9

l10 = ListNode(-5)
l9.next = l10

l10.next = l10


mySolution = Solution()
print(mySolution.detectCycle(list1head))
