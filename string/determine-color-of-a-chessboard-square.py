"""
Link: https://leetcode.com/problems/determine-color-of-a-chessboard-square/
You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

Example 1:
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:
Input: coordinates = "c7"
Output: false
 
Constraints:
coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'
"""
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        Return true if the square is white, and false if the square is black.
        """
        """
        The rule is that a/c/e/g + even number or b/d/f/h + odd number will be white, then we can check if the difference between
        char1 and a plus char2 is even or not
        """
        num1 = ord(coordinates[0]) - ord('a')
        num2 = int(coordinates[1])

        return (num1 + num2) % 2 == 0

if __name__ == '__main__':
    assert Solution().squareIsWhite('a1') == False
    assert Solution().squareIsWhite('h3') == True
    assert Solution().squareIsWhite('c7') == False