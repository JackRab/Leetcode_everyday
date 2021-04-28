"""
Link: https://leetcode.com/problems/reverse-string/

Write a function that reverses a string. The input string is given as an array of characters s.

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 
Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        """
        The idea is to sway values each pair of s, 0 VS last, 1 VS last-1
        """
        """
        Time complexity: O(n) since we loop half of the list s
        Space complexity: O(1)
        """
        n = len(s)
        middle = n // 2
        for i in range(middle):
            s[i], s[n-1-i] = s[n-1-i], s[i]
