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
        if len(chars) <= 1:
            return len(chars)

        # initialize last char and char num
        last_char = chars[0]
        char_num = 1 
        # modify chars inplace, use an index to store which index should be used
        index_chars = 0       
        for i in range(1, len(chars)):
            if last_char != chars[i]:
                # find a new char
                chars[index_chars] = last_char
                index_chars += 1
                if char_num > 1:
                    # append the num of chars
                    for j in str(char_num):
                        chars[index_chars] = j
                        index_chars += 1
                
                # reset char_num and replace last_char with the new char
                char_num = 0
                last_char = chars[i]

            char_num += 1

        # need to append last char
        chars[index_chars] = last_char
        index_chars += 1
        if char_num > 1:
            # append the num of chars
            for j in str(char_num):
                chars[index_chars] = j
                index_chars += 1

        return index_chars

