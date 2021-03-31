"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]

Constraints:
0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Return all possible letter combinations that the number could represent
        """
        """
        We can use string concatenation to combine each possible string
        """
        """
        Time complexity: O(n*4^n)
        Space complexity: O(4^n)
        """
        dict_d = {'2':'abc', '3':'def', '4':'ghi',
                 '5':'jkl', '6':'mno', '7':'pqrs',
                 '8':'tuv', '9':'wxyz'}

        res = [''] if digits else []

        for d in digits:
            res = [p + q for p in res for q in dict_d[d]]
    
        return res

if __name__ == '__main__':
    assert Solution().letterCombinations('23') == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert Solution().letterCombinations('7') == ["p","q","r","s"]