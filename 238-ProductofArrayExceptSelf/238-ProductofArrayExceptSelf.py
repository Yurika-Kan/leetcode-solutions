# Last updated: 8/21/2025, 6:28:53 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # U: create another list with product of all elements - nums[i]
        # M: array, right <-> left
        # P: 
        # store prefixes for each index w out curr index ->
        # store suffices for each index w out curr index <-
        # if beg or end, 1 
        # multiple pre & suf at end 

        # prefix -> 
        prefix = [1] * len(nums)
        for i in range(1, len(nums)): 
            prefix[i] = prefix[i-1]*nums[i-1]
        print(prefix)

        # suffix <-
        suffix = [1] * len(nums)
        for i in range(len(nums)-2, -1, -1): 
            suffix[i] = suffix[i+1]*nums[i+1]

        products = []
        for pre, suf in zip(prefix, suffix):
            products.append(pre * suf)
        return products

    # Time Complexity: O(n) where n is the len of the list 
    # Space Complexity: O(n) holding the prefix & suffix lists