"""
Link: https://leetcode.com/problems/split-a-string-in-balanced-strings/

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it in the maximum amount of balanced strings.

Return the maximum amount of split balanced strings.

 

Example 1:

Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Constraints:

1 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        Return the maximum amount of split balanced strings.
        """
        """
        Time complexity: O(n)
        Space complexity: O(1)
        """
        num_balanced = 0
        num_left = 0
        num_right = 0
        for c in s:
            if c == 'L':
                num_left += 1

            if c == 'R':
                num_right += 1
            
            if num_right == num_left and num_left >= 1:
                num_balanced += 1
                num_left = num_right = 0

        return num_balanced

if __name__ == '__main__':
    assert Solution().balancedStringSplit('RLRRLLRLRL') == 4
    assert Solution().balancedStringSplit('RLLLLRRRLR') == 3
    assert Solution().balancedStringSplit('LLLLRRRR') == 1
    assert Solution().balancedStringSplit('RLRRRLLRLL') == 2