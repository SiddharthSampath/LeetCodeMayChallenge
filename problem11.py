'''
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].
'''
'''
Approach : Graph Problem. Similar to river sizes problem but a bit simpler.
Can you breadth first search starting from sr,sc which are given. Add [sr,sc] to a queue and keep adding adjacent nodes to the queue checking if their color = initial color of image[sr][sc]
keep removing elements from the queue until it is empty.
Time Complexity : O(n) where n is the number of elements in matrix
Space Complexity : O(n) - for the visited matrix
'''

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visited = [[0 for j in range(cols)] for i in range(rows)]
        
        current = [[sr,sc]]
        oldColor = image[sr][sc]
        
        while len(current) > 0:
            x, y = current.pop(0)
            visited[x][y] = 1
            image[x][y] = newColor
            adjacentNodes = self.getAdjacent(x, y, image, visited, oldColor)
            current += adjacentNodes
        return image
    
    def getAdjacent(self,x:int, y:int, image:List[List[int]], visited : List[List[int]], oldColor : int) -> List[int]:
        adjacent = []
        if x > 0:
            if image[x - 1][y] == oldColor and not visited[x - 1][y]:
                adjacent.append([x - 1, y])
        
        if x < len(image) - 1:
            if image[x + 1][y] == oldColor and not visited[x + 1][y]:
                adjacent.append([x + 1, y])
                
        if y > 0:
            if image[x][y - 1] == oldColor and not visited[x][y - 1]:
                adjacent.append([x, y - 1])
        if y < len(image[0]) - 1:
            
            if image[x][y + 1] == oldColor and not visited[x][y + 1]:
                adjacent.append([x, y + 1])
        
        return adjacent
                
                
        
            
            
        
