'''
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1
'''
'''
Approach : Dynamic Programming. Go through the examples element by element as you would in a double for loop.
Whenever a 1 is seen, check its 3 neighbouring elements[left, top, left-top]. These will determine if this one is a part of a bigger square.
The formula which can be come up with is matrix[i][j] = 1 + min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1])
Time Complexity : O(mn) Space : O(1)- optimized
'''



class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        numOfSquares = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        numOfSquares += 1
                    else:
                        squareSize = 1 + min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
                        matrix[i][j] = squareSize
                        numOfSquares += squareSize
        return numOfSquares
    
        
#         result = [[0 for j in range(cols + 1)]for i in range(rows + 1)]
        
#         numOfSquares = 0
#         for i in range(1,rows + 1):
#             for j in range(1,cols + 1):
#                 if matrix[i - 1][j - 1] == 1:
#                     result[i][j] = 1 + min(result[i - 1][j], result[i][j - 1], result[i - 1][j - 1])
                    
#                     numOfSquares += result[i][j]
#         return numOfSquares
