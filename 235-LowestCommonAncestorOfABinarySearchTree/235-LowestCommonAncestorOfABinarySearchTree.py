# Last updated: 11/1/2025, 4:59:17 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # U: find closest ancestor of the 2 nodes, find where the split occurs
        # M: BST, < / >, recursion 
        # can't be ancestor if in diff subtree
        # left or right 
        # root is always ancestor
        curr = root
        
        # iterate till find result or tree ends
        while curr: 
            # both greater -> right subtree
            if p.val > curr.val and q.val > curr.val: 
                # point to right 
                curr = curr.right
            # both lesser -> left subtree
            elif p.val < curr.val and q.val < curr.val: 
                curr = curr.left
            # found p or q
            else: 
                return curr
        # go to deeper subtree. if not both in same subtree, found ancestor!
    
    #Time Complexity: O(log n) - height of tree
    #Space Complexity: O(1) - no data structures