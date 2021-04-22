"""
Link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

Given an integer number n, return the difference between the product of its digits and the sum of its digits.
 

Example 1:

Input: n = 234
Output: 15 
Explanation: 
Product of digits = 2 * 3 * 4 = 24 
Sum of digits = 2 + 3 + 4 = 9 
Result = 24 - 9 = 15
Example 2:

Input: n = 4421
Output: 21
Explanation: 
Product of digits = 4 * 4 * 2 * 1 = 32 
Sum of digits = 4 + 4 + 2 + 1 = 11 
Result = 32 - 11 = 21
 

Constraints:

1 <= n <= 10^5
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        """
        The idea is to loop over each digit of n, calculate their sum and product
        """
        """
        Time complexity: O(N) where N is the number of digits in n
        Space complexity: O(1)
        """
        sum = 0
        product = 1
        while n != 0:
            # get the rightmost digit of n
            d = n % 10
            sum += d 
            product *= d 
            
            # update n by eliminate the right digit of n
            n = n // 10

        return product - sum 

if __name__ == '__main__':
    assert Solution().subtractProductAndSum(234) == 15
    assert Solution().subtractProductAndSum(4421) == 21