'''
Q7. Longest Palindromic Substring

Problem Description

Given a string A of size N, find and return the longest palindromic substring in A.

Substring of string A is A[i...j] where 0 <= i <= j < len(A)

Palindrome string:
A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.

Incase of conflict, return the substring which occurs first ( with the least starting index).

Problem Constraints

1 <= N <= 10000



Input Format

First and only argument is a string A.



Output Format

Return a string denoting the longest palindromic substring of string A.



Example Input

A = "aaaabaaa"

Example Output

"aaabaaa"


Example Explanation

We can see that longest palindromic substring is of length 7 and the string is "aaabaaa".

'''

class Solution:
	def check_palindrome(self, A, i, j):
		while (i >= 0 and j < len(A) and A[i] == A[j]):
				i -= 1
				j += 1
		return i, j

	# @param A : string
	# @return a strings
	def longestPalindrome(self, A):
		length = len(A)
		max_length = 1
		res = A[0]
		for i in range(len(A)):
			#odd palidrome check
			p, q = self.check_palindrome(A, i, i)
			if max_length < q - p + 1:
				max_length = q - p + 1
				res = A[p+1:q]

			#even palindrome check
			p, q = self.check_palindrome(A, i, i+1)
			if max_length < q - p + 1:
				max_length = q - p + 1
				res = A[p+1:q]

		return res
