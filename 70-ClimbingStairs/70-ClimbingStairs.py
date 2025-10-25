# Last updated: 10/25/2025, 4:46:43 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        # Understand: given an int, return the amt of choices of steps i can take to climb these
        # input: 
        # output: 

        # edge: 
        # stair = 1 -> 1 
        # stair = 2 -> 2
        # stair = 3 

        # Match: bottom up 1dp, memoization (cache),fibonnaci, add prev way values 

        # always counter = 1 bc any numb can be with 1
        one, two = 1, 1

        # continuously update variables 
        for i in range(n-1):
            temp = one
            # update one to be sum of prev two 
            one = one + two 
            # shift two left 
            two = temp
        # at beginning - 0 
        return one

    # Time C: O(n)
    # Space C: O(1)