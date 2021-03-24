"""
Link: https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

Example 1:
Input: x = 4
Output: 2

Example 2:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1
"""

class Solution:
    def mySqrt(self, x):
        """
        Return the integer part of sqrt x
        """
        """
        The idea is use binary search that use two walls, |floor and ceiling|, to approach the square root
        """
        """
        Time complexity: O(log x), every time we half the number of elements
        Space complexity: O(1)
        """
        floor, ceiling= -1, x+1

        # when there is no integer between two walls: |floor ceiling|, we are done
        while floor+1 < ceiling:
            distance = ceiling - floor
            guess = floor + distance // 2

            if guess**2 > x:
                ceiling = guess
            if guess**2 == x:
                return guess
            if guess**2 < x:
                floor = guess

        return floor

if __name__ == '__main__':
    assert Solution().mySqrt(101) == 10
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(0) == 0