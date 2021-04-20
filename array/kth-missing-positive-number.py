"""
Link: https://leetcode.com/problems/kth-missing-positive-number/

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""
from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        The idea is to search from 1 upwards and an index for the arr, if we find one number in arr, 
        move the index in array to one step right, and that the number we want to compare next until
        we reach k
        """
        """
        Time complexity: O(n) where n is len(arr) + k
        Space complexity: O(1)
        """
        loop = 1
        index = 0
        count = 0
        while True:
            if index < len(arr) and loop == arr[index]:
                index += 1
            else:
                count += 1
            
            if count == k:
                break

            # update loop for next number
            loop += 1

        return loop

if __name__ == '__main__':
    assert Solution().findKthPositive([1, 2, 3, 4], 2) == 6
    assert Solution().findKthPositive([2,3,4,7,11], 5) == 9