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

def removeElement(nums: List[int], val: int) -> int:
    # a solution is to find the max of nums and replace all val in nums with max+1, then sort nums ascending in place
    # time complexity: sort is O(n logn), the other two for loops in O(n), so total time complexity is O(n logn)
    # space complexity: O(1)
    
    if not nums:
            return 0

    # first find the max of nums
    max_nums = nums[0]
    for n in nums:
        max_nums = max(max_nums, n)
    # then replace val in nums with max_nums + 1 and calculate the returned length
    # init length as the length of nums, then substract the number of appearance of val in nums
    length = len(nums)
    for i in range(len(nums)):
        if nums[i] == val:
            nums[i] = max_nums + 1
            length -= 1
    # sort nums in place
    nums.sort()
    return length 


