# Last updated: 5/18/2025, 1:52:25 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # empty hashmap 
        twoSumMap = {}
        result = []
        # pointer 
        i = 0

        # if diff is not in alr seen list, add it & continue
        # else if diff is in alr seen list, return that index & curr pointer
        while i < len(nums):
            diff = target - nums[i]
            if diff not in twoSumMap: 
                twoSumMap[nums[i]] = i
                i += 1
            else: 
                return [twoSumMap[diff], i]

# Time Complexity: O(n)
# Space Complexity: O(n)