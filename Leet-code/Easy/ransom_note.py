# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# https://leetcode.com/problems/ransom-note/

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countRansomeNote = Counter(ransomNote)
        countMag = Counter(magazine)

        print(countRansomeNote['d'])
        for char in countRansomeNote:
            if countRansomeNote[char] > countMag[char]:
                return False

        return True


mySolution = Solution()
ransomNote = "bg"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
print(mySolution.canConstruct(ransomNote, magazine))
