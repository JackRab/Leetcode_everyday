"""
Link: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"
 
Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Return the longest palindromic substring of s
        """
        """
        The idea is that if we find a palindrome, then a longer one containing this one must have the same char added from both end
        e.g. b-> aba -> xabax, 
        """
        """
        Time complexity: O(n^2)
        Space complexity: O(n^2)
        """
        res = ''
        for i in range(len(s)):
            # even case like 'aa'
            tmp = self.expandAndCheck(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp

            # odd case like 'aba'
            tmp = self.expandAndCheck(s, i, i)
            if len(tmp) > len(res):
                res = tmp

        return res

    def expandAndCheck(self, s: str, l, r):
        while l>=0 and r<=len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1

        return s[l+1:r]

if __name__ == '__main__':
    assert Solution().longestPalindrome('abac') == 'aba'
    assert Solution().longestPalindrome('cabac') == 'cabac'
    assert Solution().longestPalindrome('a') == 'a'