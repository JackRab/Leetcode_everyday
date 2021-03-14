"""
Link: https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
"""

from typing import List 
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Return the sum of the contiguous subarray which has the largest sum
        """
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [0]*n
        dp[0] = nums[0]
        result = dp[0]

        for i in range(1, n):
            # at each step, check if previous dp is less than zero, 
            # if yes, start dp from the current num
            if dp[i-1] < 0:
                dp[i] = nums[i]
            # if not, add previous dp to current num
            else:
                dp[i] = dp[i-1] + nums[i]

            result = max(result, dp[i])

        return result

#sol = Solution()
#sol.maxSubArray(nums = [-2,1,-3,4,-1,2,1,-5,4])