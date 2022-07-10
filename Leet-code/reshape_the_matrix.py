# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix
# Otherwise, output the original matrix.


# Example 1:


# Input: mat = [[1, 2], [3, 4]], r = 1, c = 4
# Output: [[1, 2, 3, 4]]

# https://leetcode.com/problems/reshape-the-matrix/

from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        cm = len(mat[0])
        if r*c != len(mat)*cm:
            return mat

        out = [[] for i in range(r)]
        for i in range(r*c):
            out[i//c].append(mat[i//cm][i % cm])
        return out


mat = [[1, 2, 3], [4, 5, 6]]
r = 3
c = 2
mySolution = Solution()
print(mySolution.matrixReshape(mat, r, c))
