# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

from sqlite3 import Row
from time import clock_getres
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # Linear Search
        # for row in matrix:
        #     if row[-1] >= target:
        #         return target in row
        # return False

        # print(matrix[0:1])

        # Binary Search
        def binarySearch(matrix, target):

            if len(matrix) == 0:
                return False

            midI = len(matrix)//2 if len(matrix) > 1 else 0
            midRow = matrix[midI]

            if(midRow[0] <= target and midRow[-1] >= target):
                return target in midRow
            elif target < midRow[0]:
                return binarySearch(matrix[0:midI], target)
            else:
                return binarySearch(matrix[midI+1:len(matrix)], target)

        return binarySearch(matrix, target)


mySolution = Solution()
# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
matrix = [[1]]
target = 0
print(mySolution.searchMatrix(matrix, target))
