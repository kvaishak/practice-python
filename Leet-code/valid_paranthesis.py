# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        ms = []
        mapp = {')': '(', ']': '[', '}': '{'}

        for chx in s:
            if len(ms) and mapp.get(chx) == ms[-1]:
                ms.pop()
                continue
            ms.append(chx)

        return len(ms) == 0


s = "()[]{}}"
mySolution = Solution()
print(mySolution.isValid(s))
