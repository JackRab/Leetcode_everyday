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
        First suppose we could create a new array of length m+n
        """
        if not nums1:
            return nums2
        if not nums2:
            return nums1

        new_array = [None]*(m+n)

        index_1, index_2 = 0, 0
        for i in range(m+n):
            if (index_1<=m-1) and (nums1[index_1] <= nums2[index_2]):
                new_array[i] = nums1[index_1]
                index_1 += 1
            else:
                new_array[i] = nums2[index_2]
                index_2 += 1

        return new_array

if __name__ == '__main__':
    assert Solution().merge([1, 2, 3], 3, [2, 3, 4], 3) == [1, 2, 2, 3, 3, 4]