'''
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
'''
Approach
Coming up with the naive approach is simple. Iterate over the numbers and find the binary rep at each point and count the number of ones
But this runs in O(n * (sizeOf(n))) . Too Slow. The optimal solution requires a pretty clever observation.
We can write out the binary representation of numbers (say 1 to 16) to find the pattern.
One thing we can observe is that, number of ones of 2 ^ 1, 2 ^ 2, 2 ^ 3.. are all the same, i.e 1.
We see that for even numbers, numberofones(i) = numberofones(i//2) or numberofones(i >> 2)
for odd numbers it is numberofones(i >> 2) + 1.
P.S A way to find out if a number is even or odd using bitwise operations, is to AND the number with 1. If the result is 1, it is odd. If not, even.

Time Complexity : O(n)
Space Complexity : O(n)
'''

class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0] * (num + 1)
        for i in range(1,num + 1):
            result[i] = result[i >> 1] + int(1 & i)
        
        return result
