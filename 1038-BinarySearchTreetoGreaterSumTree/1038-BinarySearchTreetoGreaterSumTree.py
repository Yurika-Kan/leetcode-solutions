# Last updated: 11/5/2025, 1:30:29 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    # reverse in order traversal - from right (largest) to left (smallest)
    # keep total sum of all nodes seen so far 
    # as visit each node, update val by adding current sum to val & updating sum to new val

    # global sum
    def __init__(self):
        self.sum = 0

    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Understand: given a root & node, k
        # bfs 
        if root: 
            # go thru right subtree & accumulate
            self.bstToGst(root.right)
            # sum accumulated val w/ my self 
            self.sum += root.val 
            # update current node val
            root.val = self.sum
            # traverse left subtree
            self.bstToGst(root.left)
        return root 

    # Time C: O(n) where n is num of nodes in bst
    # Space C: O(h) where h is height of tree

        sum += root.val 
        root.val = sum

        