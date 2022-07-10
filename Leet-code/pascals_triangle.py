
# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# Example 1:

# Input: numRows = 5
# Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

# https: // leetcode.com/problems/pascals-triangle/

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        myPas = []
        for i in range(1, numRows+1):
            tempArr = []

            for j in range(0, i):
                if j == 0 or j == i-1:
                    tempArr.append(1)
                else:
                    tempArr.append(myPas[i-2][j-1] + myPas[i-2][j])

            myPas.append(tempArr)
        return myPas


numRows = 5
mySolution = Solution()
print(mySolution.generate(numRows))
