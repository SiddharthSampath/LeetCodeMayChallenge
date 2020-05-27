'''
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
'''
'''
Approach : Whenever a 1 is encountered increment count by 1 and add it to hash table. Decrement by 1 when 0 is encountered.
Key Takeaway : Whenever we get a count that has already been encountered, between the inc=dices we have the same number of 0's and 1's

Time Complexity : O(n)
Space Complexity : O(n)
'''


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #[0,1,0]
        counter = {}
        counter[0] = -1
        
        count = 0
        maxArray = 0
        for i,num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1
            
            if count in counter:
                maxArray = max(maxArray, i - counter[count])
            else:
                counter[count] = i
        return maxArray
        
