"""
Link: https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
"""

from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Return indices of the two numbers such that they add up to target
        """
        """
        The idea is to first create a dict to store every num in the list, with the num as key and its index as value, 
        then loop to see if the complement of the num is in the dict
        """
        """
        Time complexity: O(n) since we loop over nums once (search the dict is O(1))
        Space complexity: O(n) to create the dict
        """
        dict_nums = {}
        res = [-1, -1]

        for i, n in enumerate(nums):
            c = target - n
            if c in dict_nums:
                res[0] = dict_nums[c]
                res[1] = i

            dict_nums[n] = i
            
        return res

if __name__ == '__main__':
    assert Solution().twoSum([2,7,11,15], 9) == [0, 1]
    assert Solution().twoSum([3, 2, 4], 6) == [1, 2]
    assert Solution().twoSum([3, 3], 6) == [0, 1]
    assert Solution().twoSum([3, 3], 5) == [-1, -1]