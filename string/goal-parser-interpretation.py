"""
Link: https://leetcode.com/problems/goal-parser-interpretation/
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", 
"()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", 
and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:
Input: command = "(al)G(al)()()G"
Output: "alGalooG"

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
"""

class Solution:
    def interpret(self, command: str) -> str:
        """
        Return the Goal Parser's interpretation of command
        """
        """
        The idea is to loop over the str to find patterns 
        """
        """
        Time complexity: O(n) as we loop over the string
        Space complexity: O(n)
        """
        n = len(command)
        res = []

        num_left = n
        while num_left > 0:
            if command[n-num_left] == 'G':
                res.append('G')
                num_left -= 1
            else:
                if num_left>=2:
                    if command[n-num_left:n-num_left+2] == '()':
                        res.append('o')
                        num_left -= 2
                    else:
                        res.append('al')
                        num_left -= 4

        return ''.join(res)

if __name__ == '__main__':
    assert Solution().interpret("G()(al)") == "Goal"
    assert Solution().interpret("G()()()()(al)") == "Gooooal"
    assert Solution().interpret("(al)G(al)()()G") == "alGalooG"