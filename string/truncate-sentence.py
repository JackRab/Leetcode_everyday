"""
Link: https://leetcode.com/problems/truncate-sentence/

A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. 
Return s​​​​​​ after truncating it.

Example 1:
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation:
The words in s are ["Hello", "how" "are", "you", "Contestant"].
The first 4 words are ["Hello", "how", "are", "you"].
Hence, you should return "Hello how are you".

Example 2:
Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"
Explanation:
The words in s are ["What", "is" "the", "solution", "to", "this", "problem"].
The first 4 words are ["What", "is", "the", "solution"].
Hence, you should return "What is the solution".

Example 3:
Input: s = "chopper is not a tanuki", k = 5
Output: "chopper is not a tanuki"
 
Constraints:
1 <= s.length <= 500
k is in the range [1, the number of words in s].
s consist of only lowercase and uppercase English letters and spaces.
The words in s are separated by a single space.
There are no leading or trailing spaces.
"""

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        """
        Return the sentence after truncating it
        """
        """
        The idea is to separate s into words and then concatenate the first k words into a sentence
        """
        """
        Time complexity: O(n) where n is the number of chars in the string
        Space complexity: O(n) since the number of words is proportional to the number of chars
        """

        words = s.split(' ')
        return ' '.join(words[:k])

if __name__ == '__main__':
    assert Solution().truncateSentence("Hello how are you Contestant", 4) == "Hello how are you"
    assert Solution().truncateSentence("What is the solution to this problem", 4) == "What is the solution"
    assert Solution().truncateSentence("chopper is not a tanuki", 5) == "chopper is not a tanuki"