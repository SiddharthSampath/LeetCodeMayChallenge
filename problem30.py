'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

 

Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)
'''
'''
Approach
One way to solve this problem is to find th euclidean distance of all points and sort them.
Then we can return the first k points.
Time Complexity : O(nlogn)
Space : O(1)

Another approach is to use quickselect. This can be used as the order of the output does not matter.
Once we put the kth element in the correct position we can just return the first k elements.
Time Complexity : O(n) on average. Worst Case : O(n^2)
Space : O(1)
'''
class Solution:
    # [[3,3],[5,-1],[-2,4]]
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        for point in points:
            ed = math.sqrt((point[0] ** 2) + (point[1] ** 2))
            point.append(ed)
        
        points.sort(key = lambda x:x[2])
        res = []
        for i in range(K):
            res.append([points[i][0],points[i][1]])
        return res

#         for point in points:
#              ed = math.sqrt((point[0] ** 2) + (point[1] ** 2))
#              point.append(ed)
#         #print(points)
#         res = self.quickSelect(points, 0, len(points) - 1, K)
#         for point in res:
#             pointpop = point.pop()
#         return res
    
    
#     def quickSelect(self, points : List[List[int]], low : int, high : int, K : int) -> List[List[int]]:
#         #[[3, 3, 4.242640687119285], [5, -1, 5.0990195135927845], [-2, 4, 4.47213595499958]]
#         while True:
#             pivot = low
#             i = low + 1
#             j = high
#             while i <= j:
#                 if points[i][2] > points[pivot][2] and points[j][2] < points[pivot][2]:
#                     self.swap(points,i,j)

#                 if points[i][2] <= points[pivot][2]:
#                     i += 1

#                 if points[j][2] >= points[pivot][2]:
#                     j -= 1

#             self.swap(points, pivot, j)
#             #print(points)
#             if j == K - 1:
#                 return points[:j + 1]
#             if j > K - 1:
#                 high = j - 1
#             else:
#                 low = j + 1
    
#     def swap(self, points : List[List[int]], i, j):
#         points[i], points[j] = points[j], points[i]
