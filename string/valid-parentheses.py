"""
Link: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Return if the input string is valid
        """
        """
        The idea is to use a stack to store open left parentheses and every time we find a right parenthesis check if there is 
        a paired left parenthesis (pop)
        """
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
        stack_parentheses = []

        for c in s:
            if c in ['(', '[', '{']:
                stack_parentheses.append(c)
            else:
                if stack_parentheses:
                    last_parenthesis = stack_parentheses.pop()

                    if (last_parenthesis, c) not in [('(', ')'), ('[', ']'), ('{', '}')]:
                        return False
                else:
                    return False

        return len(stack_parentheses) == 0
            
if __name__ == '__main__':
    assert Solution().isValid('()') == True
    assert Solution().isValid('()[]{}') == True
    assert Solution().isValid('(]') == False
    assert Solution().isValid('([)]') == False
    assert Solution().isValid('{[]}') == True
    assert Solution().isValid('}') == False