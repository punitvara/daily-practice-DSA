'''
Q2. Special Subsequences "AG"

Problem Description

You have given a string A having Uppercase English letters.

You have to find that how many times subsequence "AG" is there in the given string.

NOTE: Return the answer modulo 109 + 7 as the answer can be very large.



Problem Constraints

1 <= length(A) <= 105



Input Format

First and only argument is a string A.



Output Format

Return an integer denoting the answer.



Example Input

Input 1:

 A = "ABCGAG"
Input 2:

 A = "GAB"


Example Output

Output 1:

 3
Output 2:

 0


Example Explanation

Explanation 1:

 Subsequence "AG" is 3 times in given string
Explanation 2:

 There is no subsequence "AG" in the given string.
'''

# For every G, you need to count A appeared before. Add number of A appeared before G, everytime G appears.

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        length = len(A)
        count = 0
        s = 0
        for i in range(length):
            if A[i] == 'A':
                count += 1
            if A[i] == 'G':
                s += count
        return s
