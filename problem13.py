'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

'''
'''
Approach:

A slightly harder problem. A naive solution is too try removing each element in the number one by one and check which leads to the lowest possible number.
Then take that number find the next number to remove... and so on till k elements are removed.
Time : O(kn) Space O(1)

Optimal Solution : One thing to realize by looking at multiple examples is that if the number just before the number we are at is greater than the current num, we can remove the previous number. If we have not removed k elements using this approach, that means either all the digits in the number are the same or the digits are in ascending order.
In either case, we can just remove the last k digits from the number.
For this approach we can use a stack. We can push digits onto the stack, and if at any point the current digit is less than the top of the stack, we pop.
Keep decrementing k as we pop. If k is not 0 after going through all the digits, the last k letter in the stack cam be removed.
'Time : O(n) Space : O(n)
'''
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return "0"
        if len(num) == 0:
            return "0"
        stack = []
        for i in range(len(num)):
            while stack and k > 0 and stack[-1] > num[i]:
                
                stack.pop()
                k -= 1
            stack.append(num[i])
                    
        print(k)
        res = "".join(stack[0:len(stack) - k])
        print(res)
        res = res.lstrip("0")
        if len(res) > 0:
            return res
        return "0"
        return res
