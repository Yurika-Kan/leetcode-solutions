# Last updated: 3/25/2026, 10:55:17 AM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        result = []
4        prefix = 1
5        
6        for i in range(len(nums)):
7            result.append(prefix)
8            prefix = prefix * nums[i]
9
10        suffix = 1
11        for i in range(len(nums)-1, -1, -1):
12            result[i] = result[i] * suffix
13            suffix = suffix * nums[i]
14
15        return result
16
17    # Time: O(n)
18    # Space: O(n)
19