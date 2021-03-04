"""
Link: https://leetcode.com/problems/count-primes/
Count the number of prime numbers less than a non-negative number, n. 

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
 

Constraints:

0 <= n <= 5 * 10**6
"""

def countPrimes(n):

    if n<= 2:
        return 0

    primes = [True]*n
    primes[0] = primes[1] = False
    # the idea is to mark off numbers that are divisible by a prime number
    # start from 2, starting mark off number is i^2 with increment of i
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            # i is a prime, mark off all numbers i^2 + j*i
            for j in range(i*i, n, i):
                primes[j] = False
                
    return sum(primes)


