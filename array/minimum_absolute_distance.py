"""
Link: https://leetcode.com/problems/minimum-absolute-difference/

Given an array of *distinct* integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.


Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]


Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
"""

def minimun_abs_distance(arr):
    """
    Return all pairs of elements with the minimum absolute difference of any two elements
    """
    """
    The idea is to first has arr sorted ascending, then have a for loop check whether any
    too neighbor elements have the minimu distance
    """
    """
    Time complexity: sorting O(nlogn), find min distance O(n), gen list O(n), so O(n) in total
    Space complexity: use an array to store sorted arr and another array to store return list, O(n)
    """

    # sort array and store it as array_sorted
    arr_sorted = sorted(arr)

    # initialize min distance
    min_distance = arr_sorted[1] - arr_sorted[0]
    # find the min distance first
    for i in range(1, len(arr)):
        if arr_sorted[i] - arr_sorted[i-1] < min_distance:
            min_distance = arr_sorted[i] - arr_sorted[i-1]

    # init a list to store returned pairs
    ret_list = []
    for i in range(1, len(arr)):
        if arr_sorted[i] - arr_sorted[i-1] == min_distance:
            ret_list.append([arr_sorted[i-1], arr_sorted[i]])

    return ret_list

        