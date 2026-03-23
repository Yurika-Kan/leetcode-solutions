# Last updated: 3/23/2026, 5:17:49 PM
1class Solution:
2    def subarraySum(self, nums: List[int], k: int) -> int:
3        # U: find # of subarrays that sums to k 
4        # M: sliding window
5        # PI: 
6        # when would we know to move the left & right pointer?
7        
8        result = 0 
9        currSum = 0 
10        prefixSums = {0:1}
11
12        for num in nums: 
13            # check for if prefix sum to remove to get to k exists
14
15            currSum += num
16            # sum of prefix / delta diff to remove from curr window to get k
17            diff = currSum - k
18
19            # do we have a x in our prefix map that we can remove from this windows prefix to get k?
20            # for that prefixSum, how many ways of making up for it / subarray to remove
21            result += prefixSums.get(diff, 0)
22            # creating a prefixsum at current index
23            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
24
25        return result
26
27        # map - how many diff ways to sum up to #
28      
29        # Time: O(n)
30        # Space: O(n) - hashmap 