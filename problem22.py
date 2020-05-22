'''
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
'''
Approach :
When the problem is related to the frequency of characters, 1 approach which is feasible most of the time is to create a hash table containing the frequency of the characters.
This hash table can be used to created another hash table(or array of arrays of size 2 [key,val]) which is sorted by frequency(descending). Then a simple concatination of all char*freq, gives the required result.

Time : O(nlog(n)) - sorting of the hash table is required.
Space : O(n) - Hash table
'''
class Solution:
    #"tree"
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for char in s:
            frequency[char] = frequency.get(char,0) + 1
     
        sortedFrequency = {k:v for k,v in sorted(frequency.items(), key=lambda item : item[1], reverse=True)}
        
        string = ''
        for char, freq in sortedFrequency.items():
            string += (char)*freq
        return string
                                
