"""
Link: https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 
Constraints:
1 <= n <= 45
"""
class Solution:
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n):
        """
        Return distinct ways can you climb to the nth stair
        """
        """
        This is similar to fabonacci series, and solving this problem can use the same strategy
        Time complexity: O(n)
        Space complexity: O(1)
        """
        if n in [1, 2]:
            return n 

        if n in self.memo:
            return self.memo[n]

        num = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = num 
        return num

if __name__ == '__main__':
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(45) == 1836311903