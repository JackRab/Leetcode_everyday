"""
Link: https://leetcode.com/problems/remove-element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 2.
It doesn't matter what you leave beyond the returned length. For example if you return 2 with nums = [2,2,3,3] or 
nums = [2,2,0,0], your answer will be accepted.

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

"""

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        A better solution is to sort nums based on whether the element is equal to val
        and then return the index of first val in nums
        """
        """
        Time complexity: O(NlogN) since we need to sort nums
        Space complexity: O(1)
        """
        nums.sort(key=lambda x: x == val)

        if val in nums:
            return nums.index(val)
        else:
            return len(nums)


