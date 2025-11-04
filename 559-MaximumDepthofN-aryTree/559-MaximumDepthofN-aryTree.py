# Last updated: 11/4/2025, 12:28:24 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # Understand: given a node root, return max depth of tree
        # levels separated by null 
        # dfs

        # root 
        def dfs(node, depth): 
            # end of tree level - null / empty 
            if not node: 
                return 0
            # at the leaf, val but no kids - calculated depth
            if not node.children: 
                return depth
            # max depth of my children 
            return max(dfs(child, depth+1) for child in node.children)
        
        if not root: 
            return 0
        return dfs(root, 1)

        # Time C: O(n)
        # Space C: O(h) - h is heigh of tree, recursive traversal