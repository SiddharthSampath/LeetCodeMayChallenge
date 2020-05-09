'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 
'''

'''
Approach: A recursive dfs approach.
A mistake I made was I misread the question and thought it was a binary SEARCH tree.
The depth of each node can be found using a recurisve function, and when the required nodes are found, we can check if they have the same parent.
If not, return true. Time Complexity : O(n) Space : O(log(n)) on average as the number of nodes in the call stack will be approximately half the number of nodes in the tree if the tree is a complete/balanced binary tree
'''

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        depth = 0
        xDepth,parent1 = self.findDepth(root, None, 0, x)
        yDepth,parent2 = self.findDepth(root, None,0, y)
        
        if xDepth == yDepth:
            if parent1 == parent2:
                return False
            return True
        return False
    
    def findDepth(self, node: TreeNode,parent : TreeNode,depth: int, x: int ) -> int:
        if node == None:
            return [-1, -1]
        if x == node.val:
            return [depth, parent]
        left = self.findDepth(node.left, node, depth + 1, x)
        if left[0] == -1:
            right = self.findDepth(node.right, node, depth + 1, x)
            return right
        return left
