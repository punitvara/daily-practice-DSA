'''
Q3. Find subsequence

Given two strings A and B, find if A is a subsequence of B.

Return "YES" if A is a subsequence of B, else return "NO".


Input Format

The first argument given is the string A.
The second argument given is the string B.
Output Format

Return "YES" if A is a subsequence of B, else return "NO".
Constraints

1 <= lenght(A), length(B) <= 100000
'a' <= A[i], B[i] <= 'z'
For Example

Input 1:
    A = "bit"
    B = "dfbkjijgbbiihbmmt"
Output 1:
    YES

Input 2:
    A = "apple"
    B = "appel"
Output 2:
    "NO"
'''
#solution
class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def solve(self, A, B):
        length_A = len(A)
        length_B = len(B)

        j = 0
        for i in range(length_B):
            if A[j] == B[i]:
                j += 1

            if j == length_A:
                return "YES"
        return "NO"
