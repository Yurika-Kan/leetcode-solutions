# Last updated: 6/9/2025, 5:25:45 PM
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search through a sorted unique list for target #
        # set pointers
        left = 0 
        right = len(nums) - 1

        # while traversing list 
        while left <= right: 
            # find middle point
            mid = (left+right) // 2
            if target == nums[mid]:
                return mid
            # number is in low left half 
            elif target < nums[mid]: 
                right = mid - 1
            # number is in high right half 
            else: 
                left = mid + 1
        
        return -1

# Time Complexity: O(logn)
# Space Complexity: O(1)