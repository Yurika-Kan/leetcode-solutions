# Last updated: 10/19/2025, 3:49:43 AM
class Solution:
    # sort colors - category, partition
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Understand: given a list nums, sort in place by 0s, 1s, 2s
        # input: list nums size n 
        # output: none 
        # Match: list traversal, greedy?, mergesort, hashing, two pointers, quicksort 
        
        # library sorting func O(nlogn)
        # mergesort / quicksort O(nlogn)

        # bucketsort O(n) - only 3 diff buckets
        # partition - 0 1 2 
        # pointer left, i & switch - everything left of left is 0
        # pointer right, i & switch - everything right of right is 2 

        # Plan: 
        # initialize pointers left, right, indexing
        left, right = 0, len(nums) - 1
        i = 0

        # helper func to swap two values in list 
        def swap(a, b): 
            temp = nums[a] 
            nums[a] = nums[b]
            nums[b] = temp

        # while not pass right
        while i <= right:
            if nums[i] ==  0:  
                # put on left partition block!
                swap(left, i)
                # everything to left is 0!
                left += 1
            elif nums[i] == 2:
                # place into right partition block
                swap(i, right)
                # everything to right is 2!
                right -= 1
                # want i to be in same place so i can compare i with new right
                i -= 1 
            # increment
            i += 1

# Time C: O(n)
# Splce C: O(1)

