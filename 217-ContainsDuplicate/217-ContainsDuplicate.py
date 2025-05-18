# Last updated: 5/18/2025, 2:20:16 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

# Time Complexity: O(n)
# Space Complexity: O(n)    