# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2

# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = Counter(s)
        print(count)

        for i, chx in enumerate(s):
            if count[chx] == 1:
                return i
        return -1


mySolution = Solution()
testVal1 = "aabb"
print(mySolution.firstUniqChar(testVal1))
