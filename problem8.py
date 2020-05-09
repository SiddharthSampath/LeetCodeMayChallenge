'''
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
'''
'''
Approach : Not the type of problem I usually solve, but it just involves basic math.
Slope of all the points with reference to the reference point should be the same.
slope = y - y0 / x - x0
Corner case which I did not think about and found out only when I got an error on submitting the code is that x - x0 can be 0 causing divide by 0 error.
This should be handled.
Time Complexity : O(n) Space Complexity : O(1)
'''
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        
        originX = coordinates[0][0]
        originY = coordinates[0][1]
        
        if originX == coordinates[1][0]:
            slope = float("inf")
        else:
            slope = (coordinates[1][1] - originY) / (coordinates[1][0] - originX)
        for i in range(2, len(coordinates)):
            y = coordinates[i][1]
            x = coordinates[i][0]
            if x == originX:
                currentSlope = float("inf")
            else:
                currentSlope = (y - originY) / (x - originX)
            if currentSlope != slope:
                return False
        return True
    
        
        
