# Last updated: 3/23/2026, 12:54:58 AM
1class Solution:
2    def trap(self, height: List[int]) -> int:
3        # U: find the area of water of min left & right
4        # M: two pointer 
5        # P
6        # I
7        # R
8        # E
9
10        # edge: empty list
11        if not height: 
12            return 0
13
14        l = 0
15        r = len(height)-1
16        maxL = height[l]
17        maxR = height[r]
18        result = 0
19
20        while l < r: 
21            # if left height < right height
22            if maxL < maxR: # guarentees lower bond
23                l += 1
24                maxL = max(maxL, height[l]) # define left border
25                result += maxL - height[l] # diff between left border & me
26
27            else: 
28                r -= 1
29                maxR = max(maxR, height[r])
30                result += maxR - height[r]
31
32        return result
33
34        # Time: O(n)
35        # Space: O(n)