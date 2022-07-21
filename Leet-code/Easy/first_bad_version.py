# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.


# Example 1:

# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

# https://leetcode.com/problems/first-bad-version/

class Solution:
    def isBadVersion(self, version: int) -> bool:
        return version >= 1

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        bv = 1

        while left <= right:
            pivot = ((right-left) // 2) + left

            if self.isBadVersion(pivot) == False:
                left = pivot + 1
            else:
                bv = pivot
                right = pivot - 1

        return bv


mySolution = Solution()
print(mySolution.firstBadVersion(1))
