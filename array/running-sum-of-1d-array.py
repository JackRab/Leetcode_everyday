"""
Link: https://leetcode.com/problems/running-sum-of-1d-array/
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
Example 3:

Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]
 

Constraints:

1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Return the running sum of nums.
        """
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        running_sum = 0
        res = []
        for n in nums:
            running_sum += n
            res.append(running_sum)

        return res

if __name__ == '__main__':
    assert Solution().runningSum([1,2,3,4]) == [1,3,6,10]
    assert Solution().runningSum([1,1,1,1,1]) == [1,2,3,4,5]