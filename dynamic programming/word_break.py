"""
Link: https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

from typing import List 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Return true if s can be segmented into a space-separated sequence of one or more dictionary words
        """
        """
        The idea is the following:
        set d[0] to true and for i > 0
        for each index i: and d[i] is true if a word in the dict that ends at i-1 and d[j] is true, where j = i - len(word)
        e.g. s = "leetcode", wordDict = ["leet","code"], 
        d[4] = true because a word 'leet' ends at 3 and d[0]
        d[8] = true because a word 'code' ends at 7 and d[4] is true
        """
        """
        Time complexity: O(n*m), where m is the length of the word dict, if it's small relative to n, then O(n)
        Space complexity: O(n), use a list to indicator at an index it's true or false
        """

        d =[True] + [False]*len(s)

        for i in range(1, len(s)+1):
            for word in wordDict:
                j = i - len(word)
                if d[j]:
                    if word == s[j:i]:
                        d[i] = True

        return d[-1]