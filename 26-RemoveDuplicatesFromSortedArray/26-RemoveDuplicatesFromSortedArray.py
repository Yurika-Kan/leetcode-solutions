# Last updated: 3/23/2026, 1:24:26 PM
class Solution(object):
    def removeDuplicates(self, nums):
        # set automatically removes duplicates in nums to turn it into a set 
        # sorted modified nums into a sorted life 
        # [:] makes it traverse through the whole list of nums and update it 
        # otherwise it will be another local variable unrelated 
        nums[:] = sorted(set(nums))
        return len(nums)
        

        """
        :type nums: List[int]
        :rtype: int
        """
        