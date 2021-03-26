"""
Link: https://leetcode.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []
 
Example 3:
Input: nums = [0]
Output: []
 
Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Return all unique triplets in the array which gives the sum of zero
        """
        """
        The idea is to sort nums first, then for each element, look for two elements after that their sum is
        the negative of the num, and use a set to store any triple that has been found
        """
        """
        Time complexity: sort is O(n log n), the for loop nests the while loop makes it O(n^2)
        Space complexity: O(n)
        """
        nums.sort()
        res = []
        res_set = set()
        
        for i in range(len(nums)-2):
            start = i + 1
            end = len(nums) - 1

            a = nums[i]

            while start < end:
                b = nums[start]
                c = nums[end]
                if a + b + c == 0:
                    if tuple([a, b, c]) not in res_set:
                        res.append([a, b, c])
                        res_set.add(tuple([a, b, c]))
                    start += 1
                    end -= 1
                elif a + b + c > 0:
                    end -= 1
                else:
                    start +=1
                
        return res

if __name__ == '__main__':
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert Solution().threeSum([-2,0,0,2,2]) == [[-2,0,2]]
    assert Solution().threeSum([]) == []
    assert Solution().threeSum([0]) == []