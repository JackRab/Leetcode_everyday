"""
Link: https://leetcode.com/problems/number-of-good-pairs/

Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the number of good pairs.

Example 1:
Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

from typing import List
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        """
        The idea is to loop over the list to construct a dict that each key is a unique number,
        and each value is the number of times it appears in the list, then the number of good paris
        for each (k, v) is choose 2 from v
        """
        """
        Time complexity: O(n) since in the first loop we loop over each num in nums, while in the second loop
        we loop over a dict with at most n elements 
        Space complexity: O(n)
        """
        dict_nums = dict()
        for n in nums:
            dict_nums[n] = dict_nums.get(n, 0) + 1

        num_good_pairs = 0
        for k, v in dict_nums.items():
            if v > 1:
                num_good_pairs += (v-1)*v//2

        return num_good_pairs

if __name__ == '__main__':
    assert Solution().numIdenticalPairs([1,2,3,1,1,3]) == 4
    assert Solution().numIdenticalPairs([1,1,1,1]) == 6