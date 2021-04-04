"""
Link: https://leetcode.com/problems/relative-sort-array/

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  
Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.
 
Example 1:
Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:
1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
"""

from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2
        """
        """
        The idea is to use a hash map to store the position of number in arr2. Sort arr1 first, for elements not in arr2, 
        then assign an index to them in the hash map, then use the hash map as the key of sort function to sort arr2
        """
        """
        Time complexity: O(nlogn) since use sort twice
        Space complexity: O(n)
        """
        hash_arr2 = {v:i for i, v in enumerate(arr2)}

        arr1_sorted = sorted(arr1)
        start = len(hash_arr2)
        for n in arr1_sorted:
            if n not in hash_arr2:
                hash_arr2[n] = start 
                start += 1

        res = sorted(arr1, key=hash_arr2.get)
        return res

if __name__ == '__main__':
    assert Solution().relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]) == [2,2,2,1,4,3,3,9,6,7,19]
    assert Solution().relativeSortArray([2,3,1,3], [2,1]) == [2,1,3,3]
    assert Solution().relativeSortArray([2,3,1,3], []) == [1,2,3,3]
    assert Solution().relativeSortArray([], []) == []