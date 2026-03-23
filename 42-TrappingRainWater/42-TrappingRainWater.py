# Last updated: 3/23/2026, 1:24:25 PM
class Solution:
    def trap(self, height: List[int]) -> int:
        # U: find the area of water of min left & right
        # M: two pointer 
        # P
        # I
        # R
        # E

        # edge: empty list
        if not height: 
            return 0

        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]
        result = 0

        while l < r: 
            # if left height < right height
            if maxL < maxR: # guarentees lower bond
                l += 1
                maxL = max(maxL, height[l]) # define left border
                result += maxL - height[l] # diff between left border & me

            else: 
                r -= 1
                maxR = max(maxR, height[r])
                result += maxR - height[r]

        return result

        # Time: O(n)
        # Space: O(n)