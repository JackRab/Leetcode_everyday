"""
Link: https://leetcode.com/problems/string-compression/

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead be stored in the input character array chars. 

Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

Example 1:
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".

Example 2:
Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.

Example 3:
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Return the length of comprese string
        """
        """
        Time complexity: O(N), for loop through chars
        Space complexity: O(1), modify original chars in place
        """
        
        # index to write, and a num to count how many repetitions of current char
        i_write, num_chars = 0, 0
        for i_read, c in enumerate(chars):

            # read one more char
            num_chars += 1

            # use short-circuit evaluation to check if i_read is the last index or 
            # next char is not the same as current char
            if i_read == len(chars)-1 or chars[i_read+1] != chars[i_read]:
                chars[i_write] = chars[i_read]
                i_write += 1

                # if more than one repetitions, then need to record how many
                if num_chars > 1:
                    for j in str(num_chars):
                        chars[i_write] = j 
                        i_write += 1

                # reset num_chars to 0
                num_chars = 0


        return i_write