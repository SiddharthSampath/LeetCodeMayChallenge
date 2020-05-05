'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
'''
#Time complexity : O(n)
#Space complexity : O(min(n,A)) where A is the set of alphabets
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = dict()
        for char in s:
            frequency[char] = frequency.get(char, 0) + 1
        
        for i,char in enumerate(s):
            if frequency[char] == 1:
                return i
        return -1
