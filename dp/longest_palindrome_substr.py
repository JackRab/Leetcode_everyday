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
        if len(s) <= 1:
            return s

        # maximum store the current maximum length
        maximum = 1
        last = s[0]
        palindromes = set()
        for l in range(1, len(s)+1):
            # check if there are palindrome of length l
            for i in range(len(s)-l+1):
                if l == 1:
                    palindromes.add(s[i:i+l])
                    maximum = l
                    last = s[i:i+l]
                elif l == 2:
                    if s[i] == s[i+1]:
                        palindromes.add(s[i:i+l])
                        maximum = l
                        last = s[i:i+l]
                else:
                    if s[i] == s[i+l-1] and s[i+1:i+l-1] in palindromes:
                        palindromes.add(s[i:i+l])
                        maximum = l
                        last = s[i:i+l]

            if l - maximum > 2:
                break

        return last

if __name__ == '__main__':
    assert Solution().longestPalindrome('abac') == 'aba'
    assert Solution().longestPalindrome('cabac') == 'cabac'
    assert Solution().longestPalindrome('a') == 'a'