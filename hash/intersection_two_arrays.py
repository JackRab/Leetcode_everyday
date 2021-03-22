"""
Link: https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 
Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        The idea is to use set/hashmap to store unique element in nums1, then check if element of nums2 is in
        """
        """
        Time complexity: O(n+m) since we have to loop through nums1 (n elements)  and nums2 (m elements)
        Space complexity: O(n) since set_nums1 and intersection both proportional to nums
        """
        set_nums1 = set()

        for n in nums1:
            if n not in set_nums1:
                set_nums1.add(n)

        intersection = set()
        for i in nums2:
            if i in set_nums1:
                intersection.add(i)

        return list(intersection)

if __name__ == '__main__':
    assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert Solution().intersection([4,9, 5], [9, 4, 9, 8, 4]) == [9, 4]