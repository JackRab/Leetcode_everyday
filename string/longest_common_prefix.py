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
        Time complexity: O(len(strs[0])*N), if len(strs[0]) is short relative to N, O(N)
        Space complexity: O(1), the significant component is a list to store the longest common prefix
        """

        # the idea is to start from the first char of the first string (or the shortest string, better), 
        # check if it's the first char of other strings,
        # if yes then push it into a result list, then go to the second char,
        # if not then ends
        if not strs:
            return ""

        common_prefix = []
        len_strs = len(strs)
        for i, c in enumerate(strs[0]):
            end_or_not = False
            for s in strs[1:]:
                if len(s) < i+1:
                    end_or_not = True
                    break

                if s[i] != c:
                    end_or_not = True
                    break

            if not end_or_not:
                common_prefix.append(c)
            else:
                break

        return "".join(common_prefix)

