'''
Q1. Implement Power Function

Problem Description

Implement pow(x, n) % d.
In other words, given x, n and d,

find (xn % d)

Note that remainders on division cannot be negative. In other words, make sure the answer you return is non negative.

Input : x = 2, n = 3, d = 3
Output : 2

2^3 % 3 = 8 % 3 = 2.
'''

import sys
sys.setrecursionlimit(10**8)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0 and B ==0:
            return 0
        if B == 0:
            return 1
        half_power = self.pow(A, B//2, C)
        half_ans = ((half_power%C) * (half_power%C)) %C
        if B % 2 == 0:
            return half_ans
        else:
            return half_ans * A % C
