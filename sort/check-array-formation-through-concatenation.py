"""
Link: https://leetcode.com/problems/check-array-formation-through-concatenation/
You are given an array of distinct integers arr and an array of integer arrays pieces, 
where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. 
However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:
Input: arr = [85], pieces = [[85]]
Output: true

Example 2:
Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 3:
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 4:
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

Example 5:
Input: arr = [1,3,5,7], pieces = [[2,4,6,8]]
Output: false
 

Constraints:
1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).
"""

from typing import List
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        """
        The idea is to check each first element of pieces and find their index in arr, then concatenate pieces
        in the order of their first elements in arr, and sort pieces and combine lists in pieces into a big array
        and check if it's the same as arr
        """
        """
        Time complexity: O(n) where n is the number of lists in pieces
        Space complexity: O(n)
        """
        map_index = dict()
        for i, l in enumerate(pieces):
            if l[0] not in arr:
                return False

            map_index[i] = arr.index(l[0])

        concatenated_pieces = [] 
        for l in sorted(enumerate(pieces), key=lambda x: map_index.get(x[0])):
            concatenated_pieces.extend(l[1])

        return arr == concatenated_pieces

if __name__ == '__main__':
    assert Solution().canFormArray([85], [[85]]) == True
    assert Solution().canFormArray([15,88], [[88],[15]]) == True
    assert Solution().canFormArray([49,18,16], [[18,16,49]]) == False
    assert Solution().canFormArray([91,4,64,78], [[78],[4,64],[91]]) == True
    assert Solution().canFormArray([1,3,5,7], [[2,4,6,8]]) == False