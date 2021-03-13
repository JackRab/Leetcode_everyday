"""
Link: https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Time complexity: O(N), suppose N = n*n, since we only loop through at most (n//2+1)(n//2) approx n*n/4 times
        Space complexity: O(1)
        """
        # get the dimension of n
        n = len(matrix)

        # a general pattern is matrix[i][j] = matrix[n-1-j][i]
        for i in range(n//2 + n%2):
            for j in range(n//2):
                # store matrix[i][j] first 
                tmp = matrix[i][j]
                # for i=i, j=j, use genenal formula, i' = n-1-j, j' = i
                matrix[i][j] = matrix[n-1-j][i]
                # for i = n-1-j, j = i, -> , i' = n-1-i, j'= n-1-j
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                # for i = n-1-i, j = n-1-j, -> i' = n-1-(n-1-j) = j, j' = n-1-i
                matrix[n-1-i][n-1-j]= matrix[j][n-1-i]
                # for i = j, j = n-1-i, -> i' = n-1-(n-1-i) = i, j' = i, so it's tmp
                matrix[j][n-1-i] = tmp

