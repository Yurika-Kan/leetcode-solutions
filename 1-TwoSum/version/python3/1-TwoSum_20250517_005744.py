# Last updated: 5/17/2025, 12:57:44 AM
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # empty hashmap 
        twoSumMap = {}
        result = []
        # iterate through nums list 
        # i - pointer from 0
        i = 0

        # if not diff = target - nums[i] is in list 
        # map[nums[i], i] & i + 1
        while i < len(nums):
            diff = target - nums[i]
            if diff not in twoSumMap: 
                twoSumMap[nums[i]] = i
                i += 1
            else: 
                return [twoSumMap[diff], i]
                
