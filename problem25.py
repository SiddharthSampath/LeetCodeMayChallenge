'''
We write the integers of A and B (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers A[i] and B[j] such that:

A[i] == B[j];
The line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.

 

Example 1:


Input: A = [1,4,2], B = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will intersect the line from A[2]=2 to B[1]=2.
Example 2:

Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
Output: 2
 

Note:

1 <= A.length <= 500
1 <= B.length <= 500
1 <= A[i], B[i] <= 2000

'''

'''
Approach:
Problem sounded tricky to me at first, and felt it would have a recursive solution. Started thinking in terms of dp and creating a 2d matrix.
After going through a bunch of examples and creating the matrix, came up with a formula to fill in the values of the matrix. The problem is actually the longest common subsequence problem, put in a different way.
Exact same solution as LCS.
Time Complexity : O(mn)
Space : O(mn)
'''

class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        
        lenA = len(A)
        lenB = len(B)
        dp = [[0 for j in range(lenB + 1)] for i in range(lenA + 1)]
        
        for i in range(1,lenA + 1):
            for j in range(1, lenB + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
            
        
