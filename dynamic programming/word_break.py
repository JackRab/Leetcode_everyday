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
        The idea is to substract a word from s and see if the rest can be breaked (recursive)
        """
        print(s)
        # obtain the length of each words
        set_length = set([len(word) for word in wordDict])

        # base case
        if len(s) < min(set_length):
            return False
        
        if s in wordDict:
            return True 
        

        result = False
        for i in set_length:
            if s[:i] in wordDict:
                # use or for early termination if we have find a break, no need to continue
                result = result or self.wordBreak(s[i:], wordDict)
            
        return result

sol = Solution()
sol.wordBreak(s = "aaab", wordDict = ["a","aa","aaa"])