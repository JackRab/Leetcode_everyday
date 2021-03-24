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
        We can use Newton's method to solve this (optimization) problem
        Generally: if we want to find f(x) = 0, suppose we have an approximate answer x_k 
        then a linear approximation of f at x_k yield the function g(x) = f(x_k) + f'(x_k)(x - x_k) (by Taylor expansion)
        Let g(x) = 0 => x = x_k -f(x_k)/f'(x_k), then we can get a better answer x_k+1 and as we iterate 
        x_k will approach x* that f(x*) = 0
        Specificall: n^2 = x => n^2 - x = 0, 
        let f(n) = n^2 - x, f'(n) = 2n, f(n)/f'(n) = 1/2(n - x/n), then 
        n_k+1 = n_k - 1/2(n_k - x/n_k) = 1/2(n_k + x/n_k)
        """
        """
        Time complexity: O(log N)
        Space complexity: O(1)
        """
        n = x
        while n**2 > x:
            n = int(0.5*(n + x/n))

        return n


if __name__ == '__main__':
    assert Solution().mySqrt(10001) == 100
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(1) == 1
    assert Solution().mySqrt(0) == 0