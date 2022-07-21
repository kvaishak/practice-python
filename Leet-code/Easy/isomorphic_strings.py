# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.


# Example 1:

# Input: s = "egg", t = "add"
# Output: true

# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myDict = {}
        if len(s) != len(t):
            return False

        for i, char in enumerate(s):
            if char not in myDict:
                if t[i] in myDict.values():
                    return False
                myDict[s[i]] = t[i]
            elif myDict[s[i]] != t[i]:
                return False

        return True


mySolution = Solution()
testVal1 = "bada"
testVal2 = "aded"
print(mySolution.isIsomorphic(testVal1, testVal2))
