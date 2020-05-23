'''
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.  The intersection of two closed intervals is a set of real numbers that is either empty, or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)

 

Example 1:



Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder: The inputs and the desired output are lists of Interval objects, and not arrays or lists.
 

Note:

0 <= A.length < 1000
0 <= B.length < 1000
0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
'''

'''
Approach : Since 2 lists have to be merged, merge sort type of algo seems feasible, with tweaks to accomodate intervals in the lists.
A key observation which can be made, by taking any 2 intervals, 1 from each list, and finding the common interval is that:
To check if 2 intervals have an intersection, we can find :
low = max(A[i][0],B[j][0])
high = min(A[i][1], B[j][1])
if low <= high:
add this interval.

Then we check which interval ends with the lower number. We move that pointer forward as it can no longer be used to create another valid interval. 
Time Complexity : O(m+n) Space: O(m+n) - answer to be returned
'''
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        #  A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
        
        i = 0
        j = 0
        intervals = []
        while i < len(A) and j < len(B):
            currentI = A[i]
            currentJ = B[j]
            
            low = max(currentI[0], currentJ[0])
            high = min(currentI[1], currentJ[1])
            
            if low <= high:
                intervals.append([low,high])
            
                                    
            if currentI[1] > currentJ[1]:
                j += 1
            else:
                i += 1
                    
        return intervals
