# Last updated: 11/1/2025, 4:59:18 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # U: switch left & right each node
        # M: recursive & top down & pre-order (node, left, right, next) & DFS
        
        curr = root 
        # base case
        if curr == None: 
            return None
        else:
            #swap
            curr.left, curr.right = curr.right, curr.left
            self.invertTree(curr.left)
            self.invertTree(curr.right)
        return root

# Time Complexity: O(n)
# Space Complexity: O(n)