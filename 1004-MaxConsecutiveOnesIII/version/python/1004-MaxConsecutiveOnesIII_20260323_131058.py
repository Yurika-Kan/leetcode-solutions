# Last updated: 3/23/2026, 1:10:58 PM
1class Solution:
2    def longestOnes(self, nums: List[int], k: int) -> int:
3        # U: go through list numbers to find length of longest consecutive 1's after flipping k0's
4
5        # M: sliding window, 2 pointer
6
7        # P: 
8        # set pointers
9        l = 0
10        max_w = 0
11        num_zeros = 0
12        n = len(nums)
13
14        for r in range(len(nums)): 
15            # shift right pointer to increase width 
16            if nums[r] == 0: 
17                num_zeros += 1
18
19            # everytime we shift right pointer & encounter 0 & increase 0
20            # we check against k to see if we need to shift left pointer
21            # while window is invalid ie more zeros than k
22            while num_zeros > k:
23                # if the left pointer we want to increment was at 0, we get that back 
24                if nums[l] == 0: 
25                    num_zeros -= 1
26                # shift
27                l += 1
28
29            # window is valid -> calculate max width
30            max_w = max(max_w, r - l + 1)
31        
32        return max_w
33
34        # Time: O(n)
35        # Space: O(1)
36        
37       