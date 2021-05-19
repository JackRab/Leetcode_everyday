"""
Link: https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

Given a sentence that consists of some words separated by a single space, and a searchWord.

You have to check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

If searchWord is a prefix of more than one word, return the index of the first word (minimum index). 
If there is no such word return -1.

A prefix of a string S is any leading contiguous substring of S.

Example 1:
Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.

Constraints:
1 <= sentence.length <= 100
1 <= searchWord.length <= 10
sentence consists of lowercase English letters and spaces.
searchWord consists of lowercase English letters.
"""

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        """
        Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).
        """
        """
        The idea is to split the sentence into a list of words, then search over each word to see if there
        is a word with prefix of searchword
        """
        """
        Time complexity: O(n) where n is the number of words
        Space complexity: O(n)
        """
        words = sentence.split(' ')
        for i, word in enumerate(words, 1):
            if word.startswith(searchWord):
                return i
            
        return -1
            
if __name__ == '__main__':
    assert Solution().isPrefixOfWord('i love eating burger', 'burg') == 4           
    assert Solution().isPrefixOfWord('i love eating burger', 'urg') == -1           