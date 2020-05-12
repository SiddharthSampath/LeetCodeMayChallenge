'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
'''
'''
Approach : A simple O(n) solution is to iterate through the array checking the previous element.
But this is too simple, and can be optimized
As all numbers are repeated twice except the first one, Every number at an even index will have its repeated number at index + 1
The number at ind 0 will be repeated at ind 1.
Using binary search, we can find the mid ele. If the mid is even, check the ele after it. If they are equal, the single occurance has not occurred yet, as one single occurance will cause this condition (array[even] == array[even + 1] or array[odd] == array[odd - 1] will be false
so we search in the right half. if not we search in the left half. If mid is odd, we check if arr[mid] == arra[mid - 1] and continue the same process/
Time Complexity : O(log(n)) Space : O(1)
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        i = 0
        j = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while i <= j:
            if nums[j] == nums[j - 1]:
                j -= 2
            else:
                return nums[j]
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i]
         '''
        
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 0:
                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid 
            else:
                if nums[mid] == nums[mid - 1]:
                    left = mid + 1
                else:
                    right = mid
        return nums[left]
        
        
