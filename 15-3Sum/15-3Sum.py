# Last updated: 10/5/2025, 11:57:22 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # a + b + c = 0 
        # Understand：return 3 distinct combos of numbers that add up to zero
        # naive - 3 loop to get every combo
        # Match: pointers, nested loops, 2sum, enumerating 
        # Plan:
        # Problem - duplicates -> sort & save all combos that start w a   
        # Implement: 
        result =[]
        # sort to avid duplicates
        nums.sort()

        # gives index & value when you enumerate
        for i, a in enumerate(nums): 
            # first pointer is not first val in nums & curr num is same as prev num
            if i > 0 and a == nums[i-1]:
                # continue to next iteration loop 
                continue

            # initialize bordering l & r pointers 
            l = i + 1
            r = len(nums) - 1
            while l < r: 
                threeSum = a + nums[l] + nums[r]
                # too big, try smaller num
                if threeSum > 0: 
                    r -= 1 
                # too small, try bigger num
                elif threeSum < 0: 
                    l += 1
                else: 
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    # left pointer val is same as prev and stll in range 
                    # upper while loop takes care of moving other pointers
                    while nums[l] == nums [l-1] and l < r:
                        # increment
                        l += 1 
        return result

# Time Complexity: O(nlog n) + O(n^2) -> O(n^2)
# Space Complexity: O(n) - sorting takes 