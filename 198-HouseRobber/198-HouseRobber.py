# Last updated: 11/2/2025, 5:15:15 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Understand: given a list of ints, return max sum of non adjacent index ints
        # cases: 
        # edge: nums.length = 1 -> return nums[0]
        # nums.length = 2 -> return max(nums[i])

        # reccurence relation: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        # rob prev before me or me & the prev prev before me 
        # carry forward only the last two decisions 
        
        rob1, rob2 = 0, 0
        # rob1 - dp[i-2] - prev prev (plus me soon)
        # rob2 - dp[i-1] - prev (w/out me)

        # [rob1, rob2, n, n+1,...]
        for num in nums: 
            # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            temp = max(rob2, num + rob1)
            # rob1 -> rob2
            rob1 = rob2 
            # last val
            rob2 = temp
        # last val, max you can rob from entire houses
        return rob2
    
    # Time C: O(n)
    # Space C: O(1)

'''
        if len(nums) == 1: 
            return nums[0]
        
        if len(nums) == 2: 
            return max(nums[0], nums[1])
        
        i = 0
        res = 0
        while i in range(len(nums)):
            res = max(nums[i] + self.rob(nums[i+2:]), self.rob(nums[i+1:]))
            i += 1
        
        return res
        # base case: return max of two 
        # recurrence case: 
'''

        