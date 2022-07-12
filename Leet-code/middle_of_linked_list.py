# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:

# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        myList = []
        while head != None:
            myList.append(head)
            head = head.next

        return(myList[len(myList)//2])

        # Solution with just one pointer and half the traversal time : But apparently slower in Leetcode
        # temp = head
        # while head != None and head.next != None:
        #     head = head.next.next
        #     temp = temp.next

        # return temp


list1 = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5, ListNode(6))))))


mySolution = Solution()
print(mySolution.middleNode(list1))
