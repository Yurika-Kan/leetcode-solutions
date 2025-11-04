# Last updated: 11/3/2025, 10:05:04 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Understand: given a list of ints representing the cost at house index, calculate & return max money able to rob from non adjacent houses

        # edge cases: 
        # [1] - can rob - return num
        # [1, 2] - choose max 

        # compare excluding the first or excluding the last - we can't have both
        # nums[0] - in case it's only one entry 
        return max(nums[0], self.robbed(nums[1:]), self.robbed(nums[:-1]))
        
    # rob1, rob2 
    def robbed(self, nums):
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1,...]
        for num in nums: 
            # best to netizens 
            temp = max(rob2, rob1 + num) 
            # rob1 + num - ,e & prev prev 
            rob1 = rob2
            rob2 = temp
            # tracker - boolean to mark killed? 
        # how does rob2 hold the end result tho
        return rob2

    # Time C: O(n)
    # Space C: O(1)