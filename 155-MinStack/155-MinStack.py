# Last updated: 5/18/2025, 2:11:29 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# Time Complexity: O(n)
# Space Complexity: O(n)    