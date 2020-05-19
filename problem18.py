'''
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

Example 1:

Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False
 

Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''
'''
Time Complexity : O(S1 + 26 * S1 *(S2 - S1))
Space : O(1)

Approach : Tried multiple approaches for this one, kept getting TLE. First, naive approach of generating all permutations, and checking if anyone is present in s2. Too Slow.
Second approach, create a hash table of values in s1, iterate over s2 in increments of size s1, and check if the same letters are present in the hash table and s2. TLE.
Finally, create an array of size 26(alphabets) and store the frequency of chars in s1. Iterate over s2 for a size of s1, and create another array for frequency of s2 characters. Check if the new arrays are equal and return. Accepted.
'''


class Solution:
    
    #s1 = "ab" s2 = "eidbaooo" "eidboaoo" "adc" "dcda"
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counter = [0] * 26
        for i in range(len(s1)):
            s1Counter[ord(s1[i]) - ord('a')] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            s2Counter = [0] * 26
            for j in range(0,len(s1)):
                #print(ord(s2[j]) - ord('a'))
                if j >= len(s2):
                    break
                s2Counter[ord(s2[i + j]) - ord('a')] += 1
            if s1Counter == s2Counter:
                return True
        
        return False
                
        
#         counterS1 = {} #{"a" : 1,"b" : 1}
#         counterCopy = {}
#         for char in s1:
#             counterS1[char] = counterS1.get(char, 0) + 1
#             counterCopy[char] = counterCopy.get(char, 0) + 1
#         #print(counterCopy)
#         for i in range(len(s2)):
#             #print(i,s2[i])
#             characterCount = 0
#             startChar = s2[i]
#             if startChar in counterCopy:
#                 counterCopy[startChar] -= 1
#                 characterCount += 1
#                 for j in range(i + 1, i + len(s2)):
#                     #print("j",j,s2[j])
#                     if j >= len(s2):
#                         break
#                     currentChar = s2[j]
#                     if currentChar in counterCopy and counterCopy[currentChar] > 0:
#                         characterCount += 1 
#                         counterCopy[currentChar] -= 1
#                         #print(counterCopy)
#                     else:
#                         counterCopy = dict(counterS1)
#                         #print("counter restore",counterCopy)
#                         break
    
#                 #print("characterCount",characterCount)
#                 if characterCount == len(s1):
                    
#                     return True
#         return False
                    
#         permString = list(s1)
#         permutations = []
#         self.getPermutations(permString, [], permutations)
        
#         for permutation in permutations:
#             temp = "".join(permutation)
#             if temp in s2:
#                 return True
#         return False
    
    
#     def getPermutations(self,array, perm, permutations):
#         if array == []:
#             permutations.append(perm)
#             return
#         for i in range(len(array)):
#             newArray = array[:i] + array[i + 1:]
#             newPerm = perm + [array[i]]
#             self.getPermutations(newArray, newPerm, permutations)
