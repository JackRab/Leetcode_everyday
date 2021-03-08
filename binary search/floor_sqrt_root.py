"""
Link: https://leetcode.com/problems/sqrtx/

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only 
the integer part of the result is returned. 

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

def floor_sqrt_root(x):
    """
    return the largest integer not great than sqrt(x)
    """
    """
    time complexity: O(log(n)) since this a binary search
    space complexity: O(1), only a few variables needed
    """
    if x == 0:
        return 0

    if x == 1: 
        return 1

    min = 1
    max = x

    guess = (min + max) // 2
    while min + 1 != max:
        #print('min: {}, max: {}'.format(min, max))
        if guess**2 > x:
            max = guess

        if guess**2 == x:
            return guess

        if guess**2 < x:
            min = guess

        guess = (min + max) // 2

        #print("guess: {}".format(guess))

    return min