"""
Link: https://leetcode.com/problems/implement-strstr/

Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Example 3:
Input: haystack = "", needle = ""
Output: 0

Constraints:
0 <= haystack.length, needle.length <= 5 * 104
haystack and needle consist of only lower-case English characters.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Return the index of the first occurrence of needle in haystack

        Parameters
        ----------
        haystack : str
        needle : str

        Returns
        -------
        int: the index of the first occurrence of needle in haystack; 
             -1 if not found, 0 if needle is empty
        """
        """
        Time complexity: O(N) since we are iterating haystack
        Space complexity: O(1)
        """
        index = 0
        while index <= len(haystack) - len(needle):
            if haystack[index:index+len(needle)] == needle:
                break
            else:
                index += 1
        
        if index > len(haystack) - len(needle):
            return -1

        return index

if __name__ == '__main__':
    assert Solution().strStr('hello', 'll') == 2
    assert Solution().strStr('aaaaa', 'bba') == -1
    assert Solution().strStr('', '') == 0