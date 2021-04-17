"""
Link: https://leetcode.com/problems/increasing-decreasing-string/
Given a string s. You should re-order the string using the following algorithm:

Pick the smallest character from s and append it to the result.
Pick the smallest character from s which is greater than the last appended character to the result and append it.
Repeat step 2 until you cannot pick more characters.
Pick the largest character from s and append it to the result.
Pick the largest character from s which is smaller than the last appended character to the result and append it.
Repeat step 5 until you cannot pick more characters.
Repeat the steps from 1 to 6 until you pick all characters from s.
In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.


Example 1:
Input: s = "aaaabbbbcccc"
Output: "abccbaabccba"
Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
After steps 4, 5 and 6 of the first iteration, result = "abccba"
First iteration is done. Now s = "aabbcc" and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"

Constraints:
1 <= s.length <= 500
s contains only lower-case English letters.
"""

class Solution:
    def sortString(self, s: str) -> str:
        """
        The idea is to use store the frequency of each char, and loop over all chars from small to large and then large to small 
        (decrease frequency each time) until all frequencies each to zero
        """
        """
        Time complexity: O(n) since we use a while loop to append a string of length equal to the length of s
        Space comlexity: O(n) since we use a list res to store the new string
        """
        dict_char_freq = {}
        chars = set()
        for c in s:
            dict_char_freq[c] = dict_char_freq.get(c, 0) + 1
            chars.add(c)

        # turn the set of chars into a sorted list
        list_chars = sorted(list(chars))
        res = []
        while len(res) < len(s):
            for c in list_chars:
                if dict_char_freq[c] != 0:
                    res.append(c)
                    dict_char_freq[c] -= 1

            for c in list_chars[::-1]:
                if dict_char_freq[c] != 0:
                    res.append(c)
                    dict_char_freq[c] -= 1

        return ''.join(res)

if __name__ == "__main__":
    assert Solution().sortString("aaaabbbbcccc") == "abccbaabccba"