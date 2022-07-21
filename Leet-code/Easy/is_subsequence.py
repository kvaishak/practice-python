# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some(can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).


# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true


# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t1 = 0
        s1 = 0

        while t1 <= len(t)-1:
            if(t[t1] == s[s1]):
                s1 += 1
            t1 += 1
        return s1 == len(s)


s = "abc"
t = "ahbgdc"
mySolution = Solution()
print(mySolution.isSubsequence(s, t))
