"""
Link: https://leetcode.com/problems/maximum-69-number/

Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, 
and 9 becomes 6).

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666. 
The maximum number is 9969.

Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.
"""

class Solution:
    def maximum69Number (self, num: int) -> int:
        """
        The idea is to change the leftmost 6 to 9
        """
        """
        Time complexity: O(n) where n is the number of digits
        Space complexity: O(n)
        """
        res = list(str(num))
        for i, c in enumerate(res):
            if c == '6':
                res[i] = '9'
                break

        return int(''.join(res))

if __name__ == '__main__':
    assert Solution().maximum69Number(9669) == 9969
    assert Solution().maximum69Number(9996) == 9999
    assert Solution().maximum69Number(9999) == 9999