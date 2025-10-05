# Last updated: 10/5/2025, 11:55:35 AM
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Understand: given array of numbers, calculate maximum area from width x height combo
        # input: list of numbers 
        # output: max area 
        # Match: two pointer, min
        # Plan: 
        i = 0 
        j = len(heights)-1
        max_area = 0
        # iterate through list while pointers do not cross
        while i < j: 
            minimum_height = min(heights[i], heights[j])
            curr_area = (j-i) * minimum_height
            # update area 
            if curr_area > max_area: 
                max_area = curr_area 
            # increment 
            if heights[i] < heights[j]: 
                i += 1
            else: 
                j -= 1
        return max_area

# Time Complexity: O(n)
# Space Complexity: O(1)