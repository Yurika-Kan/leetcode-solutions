# Last updated: 5/16/2025, 8:41:07 PM
'''
Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
         
