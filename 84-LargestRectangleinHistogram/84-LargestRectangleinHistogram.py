# Last updated: 5/18/2025, 7:39:06 PM
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # pair: (index, height)
        maxArea = 0 
        # enumerate - index, val
        for i, h in enumerate(heights): 
            start = i
            # top val's height in stack > curr val height 
            while stack and stack[-1][1] > h:
                # height is too great
                index, height = stack.pop()
                # check if the popped height leads to max
                # width = curr index - start index
                maxArea = max(maxArea, height * (i - index))
                # extend start back to greater height index that we popped
                start = index
            # add start index that we possibly pushed 
            stack.append((start, h))

        for i, h in stack: 
            # end of histogram - start val i 
            maxArea = max(maxArea, h * (len(heights)-i))
        
        return maxArea
    
# iterate through, push & pop each element once
# Time Complexity: O(n)
# Space Complexity: O(n)
