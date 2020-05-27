'''
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.

 

Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false
'''
'''
A graph problem which can be solved using dfs. A dictionary can be made of the list of people a person does not like.
Then, we can iterate over each person, assign the first person to room 0. put this person on a stack, iterate over all the people he dislikes after popping top element of the stack, and check if any of these people have already been assigned rooms.
If they have check if it is the same room as person 1. if it is, return false. If not, assign this person to the other room (0^1). Add this person to the stack. Continue till stack is empty.
Time : O(N + E) - nodes + edges
Space : O(N + E)
'''
class Solution:
    
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        dictionary = collections.defaultdict(list)
        for dislike in dislikes:
            u = dislike[0]
            v = dislike[1]
            dictionary[u].append(v)
            dictionary[v].append(u)
            
        
        seen = {}
        stack = []
        for i in range(1, N + 1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while stack:
                    current = stack.pop()
                    for num in dictionary[current]:
                            if num in seen:
                                if seen[num] == seen[current]:
                                    return False
                            else:
                                seen[num] = seen[current] ^ 1
                                stack.append(num)
                        
        
        return True
    
                            
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
       
                
            
