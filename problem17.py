'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
'''
Approach: The key thing to realise is if we sort anagrams, they form the same word.
So this logic can be used here. We sort p, and at every letter in s, we sort the next p letters, and check if the strings are the same. If they are, then that is an anagram
Time Complexity : O(splog(p))
Space : O(1)
'''

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p = sorted(p) #ab
        p = "".join(p)
        result = []
        for i in range(len(s)):
            if i + len(p) <= len(s): 
                temp = sorted(s[i : i + len(p)])
                temp = "".join(temp)
                if temp == p:
                    result.append(i)
        return result
            
                
