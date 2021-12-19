'''
Problem Description

Given the root of a tree A with each node having a certain value, find the count of nodes which have more value than all its ancestor



Problem Constraints

1 <= Number of Nodes <= 200000

1 <= Value of Nodes <= 2000000000



Input Format

First and only argument of input is a tree node.



Output Format

Return a single integer denoting count of nodes which have more value than all of it's ancestor.



Example Input

Input 1:


     3
Input 2:


    4
   / \
  5   2
     / \
    3   6


Example Output

Output 1:

 1
Output 2:

 3


Example Explanation

Explanation 1:

 One node is valid
Explanation 2:

 Three nodes are 4, 5 and 6.
'''
# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    def answer(self, A, max_num):
        if A == None:
            return 0
        count = 0
        if A.val > max_num:
            max_num  = A.val
            count = 1

        left_tree = self.answer(A.left, max_num)
        right_tree = self.answer(A.right, max_num)

        return count + left_tree + right_tree
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        return self.answer(A, -math.inf)
