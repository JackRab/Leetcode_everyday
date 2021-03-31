"""
Link: https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true
 
Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
 
Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Return if two strings s and t are isomorphic
        """
        """
        The idea is to use hash to store every pair of mapping (s, t), and 
        loop over chars if the mapping exist for a char in s while not equal to what is found in t
        """
        """
        Time complexity: O(n), n is the length of string
        Space complexity: O(n)
        """
        if len(s) != len(t):
            return False

        mapping = dict()
        mapping_inverse = dict()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            else:
                mapping[s[i]] = t[i]

            if t[i] in mapping_inverse:
                if mapping_inverse[t[i]] != s[i]:
                    return False
            else:
                mapping_inverse[t[i]] = s[i]

        return True

if __name__ == '__main__':
    assert Solution().isIsomorphic('egg', 'add') == True
    assert Solution().isIsomorphic('foo', 'bar') == False
    assert Solution().isIsomorphic('paper', 'title') == True
    assert Solution().isIsomorphic('badc', 'bada') == False