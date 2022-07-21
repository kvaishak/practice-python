# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

# https://leetcode.com/problems/intersection-of-two-arrays-ii/


from collections import deque
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dnum = deque(nums1)
        intersect = []

        for _ in range(0, len(nums1)):
            temp = dnum.popleft()
            if temp in nums2:
                intersect.append(temp)
                nums2.remove(temp)

        return intersect


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
mySolution = Solution()
print(mySolution.intersect(nums1, nums2))
