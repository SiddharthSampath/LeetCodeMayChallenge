'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
'''
'''
Approach: A classic binary search question. Binary search between 1 and n / 2 to check if number*number = n.
Time Complexity : O(log(n)) Space : O(1)
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 9:
            if num == 1 or num == 4 or num == 9:
                return True
        limit = num // 4
        low = 1
        high = limit
        
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                low = mid + 1
            elif mid * mid > num:
                high = mid - 1
        return False
