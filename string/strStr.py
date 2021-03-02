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

def strStr(haystack: str, needle: str) -> int:
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
    if needle == "":
        return 0

    if len(haystack) == 0:
        return -1

    for i, s in enumerate(haystack):
        if len(haystack) - i < len(needle):
            break

        if needle == haystack[i:i+len(needle)]:
            return i

    return -1
