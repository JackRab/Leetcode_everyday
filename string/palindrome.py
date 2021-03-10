"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.

"""

def is_palindrome(s):
    """Reture is s is palindrome"""

    """
    Time complexity: O(N) since we loop over half of the elements
    Space complexity: O(1)
    """
    if not s:
        return False

    floor, ceiling = 0, len(s) - 1
    while floor < ceiling:
        #print("s[floor]: {}, s[ceiling]: {}".format(s[floor], s[ceiling]))
        # non characters, skip
        if (s[floor] < '0'
            or (s[floor] > '9' and s[floor] < 'A')
            or (s[floor] > 'Z' and s[floor] < 'a')
            or s[floor] > 'z' 
            ):
            floor += 1
            continue

        # non characters, skip
        if (s[ceiling] < '0'
            or (s[ceiling] > '9' and s[ceiling] < 'A')
            or (s[ceiling] > 'Z' and s[ceiling] < 'a')
            or s[ceiling] > 'z' 
            ):
            ceiling -= 1    
            continue

        # convert to lower case and compare, return False directly
        if s[floor].lower() != s[ceiling].lower():
            return False

        floor += 1
        ceiling -= 1

    return True

        