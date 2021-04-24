"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in 
the array nums.

Return signFunc(product).

Example 1:

Input: nums = [-1,-2,-3,-4,3,2,1]
Output: 1
Explanation: The product of all values in the array is 144, and signFunc(144) = 1
"""
from typing import List
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        """
        Time complexity: O(N) where N is the number of elements in nums
        Space complexity: O(1)
        """
        product = 1
        for n in nums:
            product *= n

        return self.signFunc(product)

    def signFunc(self, x: int) -> int:
        if x > 0:
            return 1
        if x < 0:
            return -1

        return 0