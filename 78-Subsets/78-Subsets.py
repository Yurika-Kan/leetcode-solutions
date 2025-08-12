# Last updated: 8/11/2025, 6:39:50 PM
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
    # U: return all unique subsets of num array
    # M: backtracking dfs, binary tree of choices, list/array, recursion
    # I: 
        result = []
        subset = []
        def dfs(i):
            # base case: end of tree/node
            if i >= len(nums):
                # copy of subset since subset will be modified
                result.append(subset.copy())
                return
            
            # yes! let's include nums[i] - do
            subset.append(nums[i])
            # recurse & returns after base case then moves on to backtrack 
            dfs(i+1)

            # naur.. let's not include nums[i] - undo
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result
        
    # Time Complexity: O(n * 2^n) where n is len of input array & 2^n is the 2 choices each input has 
    # Space Complexity: O(n)