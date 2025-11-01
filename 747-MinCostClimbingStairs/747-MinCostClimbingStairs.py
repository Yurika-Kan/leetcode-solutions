# Last updated: 11/1/2025, 4:59:14 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    # U: use dp to minimize cost to reach top of staircase array
    # M: DP, decision tree -> dfs, memoization/cache, recurrence & base case
        # P: backtrack iterate array to solve sub problems & find min 
        # add default end val to indicate end [a,b,c]0
        cost.append(0)
        # while index in array, start 
        # start at second to last index [len(cost) - 3] since last index will always cost same 
        # iterate this range until it reaches -1 exclusively, decrement it by -1
        for i in range(len(cost) - 3, -1, -1):
            # building out cost table 
            # curr step + min of next or next next
            cost[i] += min(cost[i+1], cost[i+2])
    
        # first or second step
        return min(cost[0], cost[1])
        
        # brute force: decision tree
        # greedy: always take 2 steps to get farther

    #Time Complexity: O(n) where n is length of array
    #Space Complexity: O(1) where 1 is just cost list
