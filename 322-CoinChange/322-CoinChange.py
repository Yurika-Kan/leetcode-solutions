# Last updated: 11/2/2025, 3:50:39 PM
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Understand: given a list of int & an int, calculate count of a combination made up of diff instances of ints that add up to target amount

        # what is min # of steps needed to each amt, where each step adds a coin's val?
        # shortest path - min path

        # cases:
        # amount / biggest coin int = does remainder exist / can be diminished to a num?
        # amount = 0 

        # Match: DP bottom up 
        # set up grid 
        dp = [amount + 1] * (amount + 1)
        print(dp)
        # takes 0 to get to amount of 0
        dp[0] = 0 
        
        # 
        for a in range(1, amount + 1):
            for coin in coins: 
                # keeps overwriting until using up all coins to get min 
                if a - coin >= 0:
                    # reccurence relation
                    dp[a] = min(dp[a], 1 + dp[a - coin])
            # coin = 4
            # a = 7 
            # dp[7] = 1 + dp[7-4] -> 1 + dp[3]

        # return amount or -1 if its still default val
        return dp[amount] if dp[amount] != amount + 1 else -1

    # Time C: O(a * n) where a is amount & n is len of coins
    # Space C: O(a)

# DP backtracking recursively with top down memoization
'''
DP through BFS
        # Match: dp & bfs - calculate subproblem 
        # bfs from 0 
        # base case: if amt = 0 -> return 0
                   # if coins empty or all > amount -> result = -1
        if amount == 0: 
            return 0 
        if not coins or min(coins)> amount: 
            return -1
        
        # bfs 
        # queue - process curr reachable totals (from 0)
        # visited set - so no recomputing total
        # steps counter - one more coin per layer 
        queue = deque([0]) 
        visited = {0}
        steps = 0 

        while queue: 
            # process curr layer 
            for _ in range(len(queue)):
                curr = queue.popleft()
                for coin in coins:
                    nxt = curr + coin
                    if nxt == amount: 
                        return steps + 1
                    if nxt < amount and nxt not in visited:
                        visited.add(nxt)
                        queue.append(nxt)
            steps +=1
    
        return - 1

# Time C: O(n * t)
# Space C: O(n)
'''

'''
Greedy with mathematical logic 
        # Match: greedy math 
        # 11 / 5 = 2 r 1 
        # 1 in coins 
        # 1 / 1 = 1 r 0 

        # [1, 3]
        # 20 / 3 = 6 r 2
        # 2 not in coins
        # 2 / 1 = 2 r 0 

        # fails here!
        # [1, 3, 4] , 6 
        # [3, 3] - not [4, 1, 1]
'''