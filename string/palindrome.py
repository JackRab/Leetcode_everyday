"""
Given a string s, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

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

    left, right = 0, len(s) - 1
    while left < right:
        #print("s[left]: {}, s[right]: {}".format(s[left], s[right]))
        # non alphanumeric, skip
        if not s[left].isalnum():
            left += 1
            continue

        # non alphanumeric, skip
        if not s[right].isalnum():
            right -= 1    
            continue

        # convert to lower case and compare, if not equal then return False directly
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

        