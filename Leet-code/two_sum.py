# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# https://leetcode.com/problems/two-sum/


from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myHash = {}
        for i, elem in enumerate(nums):
            if target-elem in myHash:
                return [myHash[target-elem], i]
            myHash[elem] = i
        return []


mySolution = Solution()
testVal1 = [2, 7, 11, 15]
testVal2 = 9
print(mySolution.twoSum(testVal1, testVal2))
