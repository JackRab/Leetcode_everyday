"""
Link: https://leetcode.com/problems/merge-sorted-array/

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively. 
You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
"""

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        Idea: from the last index of nums1 and move to the left
        """
        """
        Time complexity: O(m+n)
        Space complexity: O(1)
        """
        if not nums1:
            return
        if not nums2:
            return

        i1, i2, i = m-1, n-1, m+n-1
        while i >= 0:
            if i1 >= 0 and i2>=0:
                if nums1[i1] <= nums2[i2]:
                    # put the num from nums2 to index i
                    nums1[i] = nums2[i2]
                    i2 -= 1
                else:
                    # put the num from nums1 to index i
                    nums1[i] = nums1[i1]
                    i1 -= 1
            elif i1<0:
                nums1[i] = nums2[i2]
                i2 -= 1
            else:
                nums1[i] = nums1[i1]
                i1 -= 1
            
            i -= 1