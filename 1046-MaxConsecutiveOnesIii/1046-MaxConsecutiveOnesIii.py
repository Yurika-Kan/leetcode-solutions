# Last updated: 3/23/2026, 1:24:20 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # U: go through list numbers to find length of longest consecutive 1's after flipping k0's

        # M: sliding window, 2 pointer

        # P: 
        # set pointers
        l = 0
        max_w = 0
        num_zeros = 0
        n = len(nums)

        for r in range(len(nums)): 
            # shift right pointer to increase width 
            if nums[r] == 0: 
                num_zeros += 1

            # everytime we shift right pointer & encounter 0 & increase 0
            # we check against k to see if we need to shift left pointer
            # while window is invalid ie more zeros than k
            while num_zeros > k:
                # if the left pointer we want to increment was at 0, we get that back 
                if nums[l] == 0: 
                    num_zeros -= 1
                # shift
                l += 1

            # window is valid -> calculate max width
            max_w = max(max_w, r - l + 1)
        
        return max_w

        # Time: O(n)
        # Space: O(1)
        
       