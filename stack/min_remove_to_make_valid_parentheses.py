"""
Link: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so 
that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:
Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Return a valid string by removing minimum parentheses
        """
        """
        The idea is to use move from left to right, if find a ')' check if there is a '(' unpaired left, 
        if yes, make them a pair, if not, remove it.
        """
        """
        Time complexity: O(n), need to loop over s twice
        Space complexity: O(n), need to store parentheses
        """
        # use a list to store s
        s_list = list(s)

        # use a list as a stack to store left parentheses indexes
        parentheses = []
        for i, c in enumerate(s):
            if c == ')':
                if not parentheses:
                    # this one need to be removed
                    s_list[i] = ''
                else: # have parentheses left
                    parentheses.pop()

            if c == '(':
                parentheses.append(i)

        # remove left '('
        while parentheses:
            s_list[parentheses.pop()] = ''
        
        return ''.join(s_list)

if __name__ == '__main__':
    assert Solution().minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"
    assert Solution().minRemoveToMakeValid("a)b(c)d") == "ab(c)d"
    assert Solution().minRemoveToMakeValid("))((") == ""
    assert Solution().minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)"