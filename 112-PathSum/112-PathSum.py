# Last updated: 11/5/2025, 2:14:51 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    # Understand: given root of bt & targetSum it, return bool if root to leaf path adding up to targetSum exists 
        # invalid order - must look at every possible path 
        # in order dfs traversal - recursive

        # helper bc need changing curSum
        def dfs(node, currSum):
            # technically not node to leaf paths
            if not node: 
                return False
            currSum += node.val
            # we've arrived at a leaf node!
            if not node.left and not node.right: 
                # accumulate, was path right 
                return currSum == targetSum
            return dfs(node.left, currSum) or dfs(node.right, currSum)
        return dfs(root, 0)

    # Time C: O(n)
    # Space C: O(n) for recursion stack