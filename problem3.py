'''
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

'''
#Time Complexity : O(min(M,R)) Space : O(M)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = {}
        for char in magazine:
            magDict[char] = magDict.get(char,0) + 1
        
        for char in ransomNote:
            if char in magDict:
                if magDict[char] > 0:
                    magDict[char] -= 1
                else:
                    return False
            else:
                return False
        return True
