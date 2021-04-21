"""
Link: https://leetcode.com/problems/check-if-the-sentence-is-pangram/

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        """
        The idea is to add every char of str and check the lenght of set
        """
        """
        Time complexity: O(n) since we loop each char of the sentence
        Space complexity: O(1) since we only need a set to store at most 26 elements
        """
        chars = set()
        for c in sentence:
            chars.add(c)

        return len(chars) == 26

if __name__ == '__main__':
    assert Solution().checkIfPangram("thequickbrownfoxjumpsoverthelazydog") == True
    assert Solution().checkIfPangram("leetcode") == False