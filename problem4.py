'''
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

 

Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
 

Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
 

Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
'''

class Solution:
    def findComplement(self, num: int) -> int:
        '''
        # Time Complexity : O(log(num)) Space : O(log(num))
        binary = []
        while num > 0:
            rem = num % 2
            binary.append(rem)
            num = num // 2
        
        power = 0
        complement = 0
        ans = 0
        for num in binary:
            if num == 0:
                complement = 1
            else:
                complement = 0
            
            ans += complement * pow(2,power)
            power += 1
        return ans
        '''
        #time complexity : O(log(num)) Space Complexity : O(1)
        import math
        numBits = int(math.log2(num)) + 1
        for i in range(numBits):
            num = num ^ (1 << i)
        return num
