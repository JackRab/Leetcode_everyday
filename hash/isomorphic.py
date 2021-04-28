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

        map_st = {}
        map_ts = {}
        for c1, c2 in zip(s, t):
            if c1 in map_st:
                if map_st[c1] != c2:
                    return False
            else:
                map_st[c1] = c2

            if c2 in map_ts:
                if map_ts[c2] != c1:
                    return False
            else:
                map_ts[c2] = c1

        return True

if __name__ == '__main__':
    assert Solution().isIsomorphic('egg', 'add') == True
    assert Solution().isIsomorphic('foo', 'bar') == False
    assert Solution().isIsomorphic('paper', 'title') == True
    assert Solution().isIsomorphic('badc', 'bada') == False