# Last updated: 3/23/2026, 7:22:51 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        # O(log n) = binary search 
4        left = 0 
5        right = len(nums) - 1
6
7        while left <= right: 
8            
9            mid = (left + right) // 2
10            if nums[mid] == target: 
11                return mid
12
13        
14            if nums[left] <= nums[mid]:
15                # target is in higher part / target in rotated lower part
16                if target > nums[mid] or target < nums[left]:
17                    # Target outside left?
18                    # target > mid or < left → left
19                    # search for right/upper
20                    left = mid + 1
21                else:
22                    # Target in left range?
23                    # left <= target <= mid → right = mid-1
24                    # search for left/lower
25                    right = mid - 1
26            # right sorted portion
27            else: 
28                if target < nums[mid] or target > nums[right]: # too big 
29                    # search for left/lower
30                    right = mid - 1
31                else: 
32                    # Target in right range?
33                    # mid <= target <= right → left = mid+1
34                    left = mid + 1
35        
36        return -1
37        
38        # Time: O(log n)
39        # Space: O(1)
40
41        
42        
43        # O(n)
44        #if target in nums:
45        #    return nums.index(target)
46        #return -1