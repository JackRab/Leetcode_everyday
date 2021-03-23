"""
Link: https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-9999 <= nums[i], target <= 9999
All the integers in nums are unique.
nums is sorted in an ascending order.
"""

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Return the index of target in nums, -1 if not find
        """
        """
        The idea is to use two index, floor and ceiling to narrow down half each time
        """
        """
        Time complexity: O(log n), binary search
        Space complexity: O(1)
        """

        floor, ceiling = -1, len(nums)
        
        # if there isn't at least 1 index between floor and ceiling, 
        # we must run out of guess and number must not be present
        while floor+1 < ceiling:
            distance = ceiling - floor

            guess = floor + distance // 2
            if target == nums[guess]:
                return guess

            if target > nums[guess]:
                floor = guess
            else:
                ceiling = guess

        return -1
            


if __name__ == "__main__":
    assert Solution().search([-1,0,3,5,9,12], 9) == 4
    assert Solution().search([-1,0,3,5,9,12], 2) == -1
    assert Solution().search([-1, 1], 1) == 1
    assert Solution().search([-1, 1], -1) == 0

                