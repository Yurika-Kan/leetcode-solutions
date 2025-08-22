# Last updated: 8/22/2025, 12:47:58 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    # U: return len of the longest consecutive +1 seq 
    # M: set 
    # start val has no left neighbor
        numsSet = set(nums)
        longest = 0 
        counter = 0
        for num in numsSet: 
            # check if num is start of sequence aka no left neighbor
            if (num - 1) not in numsSet: 
                length = 0 
                # count from beginning num!
                while (num + length) in numsSet: 
                    length += 1
                # update biggest
                longest = max(length, longest)
        return longest 
    
    # Time Complexity: O(n) where n is size of input array
    # Space Complexity: O(n)
