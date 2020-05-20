'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3
Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
'''
'''
Approach:
When having to traverse a tree/graph the first thing which comes to mind is dfs/bfs/
As it is a BST, traversing the tree using inorder traversal, will give the array in sorted order.
We can return the k - 1 element from this array.
Time Complexity : O(n) Space Complexity : O(n)

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array = []
        self.inOrder(root, array, k)
        return array[k - 1]
    
    def inOrder(self, root: TreeNode, array: List, k: int):
        if root is None:
            return
        
        self.inOrder(root.left, array, k)
        array.append(root.val)
        self.inOrder(root.right, array, k)
        
