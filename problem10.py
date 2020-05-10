'''
In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.

 

Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Note:

1 <= N <= 1000
trust.length <= 10000
trust[i] are all different
trust[i][0] != trust[i][1]
1 <= trust[i][0], trust[i][1] <= N
'''
'''
Approach : Realised it was a graph problem, but did not make use of the fact the people were numbered from 1 to N. Did not do very well on this question, came up with a pretty naive solution, which became much more complicated then required.
The approach was to make a hash table with the key as the first elements in the trust array, mapping to all the people they trust/
Iterate over the hash table and check if the potentialJudge [random value picked in the beginning] is present in the current value. If it is not remove it from the potential value.
return potential judge if it is not empty.
That was exhausting to even type out.

A better approach is to count the indegree and outdegree of each element.
Create an auxilary array of size N + 1. if there is an out going edge from a particular node, decrement the value at the index of that node in the auz array. If there is an incoming edge, increment the value.
If any node has the value N - 1, that is the judge. Much more elegant solution.

Read and understand the problem thoroughly, and use all the data given to get the best solution.
Time Complexity : O(n) Space : O(n)
'''

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        '''
        outgoing = {}
        potentialJudge = []
        if trust == []:
            return 1
        for element in trust:
            if element[0] not in outgoing:
                outgoing[element[0]] = [element[1]]
            else:
                outgoing[element[0]].append(element[1])
        potentialJudge = outgoing[trust[0][0]]
        
        
        for pers, judges in outgoing.items():
            if potentialJudge == []:
                return -1
            for ele in potentialJudge:
                if ele not in judges:
                    potentialJudge.remove(ele)
                    continue
                if pers in potentialJudge:
                    potentialJudge.remove(pers)
                
        
        if potentialJudge == [] or len(potentialJudge) > 1:
            
            return -1
        else:
            
            return potentialJudge[0]
        
        '''
        
        potentialJudge = [0] * (N + 1)
        if trust == []:
            return 1
        for outT, inT in trust:
            potentialJudge[outT] -= 1
            potentialJudge[inT] += 1
        
        for i in range(len(potentialJudge)):
            if potentialJudge[i] == N - 1:
                return i
        return -1
