'''
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

'''
Approach
Dynamic Programming - Create 2d matrix of size s1 + 1 * s2 + 1.
We iterate over the strings and populate the matrix with the minimum edit distance at each point.
We can find the edit distance at each point by comparing current char in string 1 to current char in string2.
If they are equal, then no operation needs to be performed. So we can just take the value used to convert string1[:i - 1] to string2[:j - 1]
This value can be found at edits[i - 1][j - 1]
If the characters are not equal we can delete, add or substitute.
We can find these values at edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1]
adding 1 to the minimum of these values gives us our current edit distance.

Time Complexity : O(mn)
Space : O(mn)
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        edits = [[0 for j in range(len(word2) + 1)] for i in range(len(word1) + 1)]
        
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    edits[i][j] = j
                elif j == 0:
                    edits[i][j] = i
                else:
                    if word1[i - 1] == word2[j - 1]:
                        edits[i][j] = edits[i - 1][j - 1]
                    else:
                        edits[i][j] = 1 + min(edits[i - 1][j - 1], edits[i - 1][j], edits[i][j - 1])
                    
        return edits[-1][-1]
