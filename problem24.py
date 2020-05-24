'''
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.

Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]

 

Constraints:

1 <= preorder.length <= 100
1 <= preorder[i] <= 10^8
The values of preorder are distinct.

'''
'''
Approach:
The approach taken here is the same as making a BST from an array.
We can take the first element of the list as the root. Insert the remaining values into the BST in the correct position. The insertion is simple to understand from the code.
Time : O(nd) n - number of nodes, d - depth of the tree
Space : O(n) - BST space
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #[8,5,1,7,10,12]
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        rightTree = []
        leftTree = []
#         for i in range(1,len(preorder)):
#             if preorder[i] > root.val:
#                 rightTree.append(preorder[i]) #[5,1,7]
#             else:
#                 leftTree.append(preorder[i]) #[10,12]
        
#         leftRoot = self.makeBST(leftTree)
#         rightRoot = self.makeBST(rightTree)
        
#         root.left = leftRoot
#         root.right = rightRoot
        
        return self.makeBST(preorder)
    
    def makeBST(self, tree : List[int]) -> TreeNode:
        if tree == []:
            return None
        root = TreeNode(tree[0])
        
        for i in range(1, len(tree)):
            num = tree[i]
            current = root
            while True:
                if num < current.val:
                    if current.left:
                        current = current.left
                    else:
                        current.left = TreeNode(num)
                        break
                else:
                    if current.right:
                        current = current.right
                    else:
                        current.right = TreeNode(num)
                        break
                        
        return root
