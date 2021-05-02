"""
Link: https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""

def find_longest_common_prefix(strs):
        """
        Return the longest common prefix string amongst an array of strings, empty if no common prefix
        """
        """
        Time complexity: O(min_num*N), where min_num is the minimum num of chars in the strs
        Space complexity: O(1), the significant component is a list to store the longest common prefix
        """
        """
        The idea is to check from the first char to the char that is not a common component
        the maximum possible prefix is of min_num length
        """
        end = 0
        min_num = min([len(s) for s in strs])
        candidate = ''
        while end < min_num:
            if all([strs[0][end] == s[end] for s in strs[1:]]):
                candidate += strs[0][end] 
                end += 1
            else:
                break

        return candidate

