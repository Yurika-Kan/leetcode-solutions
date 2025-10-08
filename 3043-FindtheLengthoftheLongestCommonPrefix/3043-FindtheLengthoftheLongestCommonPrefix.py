# Last updated: 10/7/2025, 9:13:13 PM
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # Understand: given two lists, find length of the longest common prefix
        # edge: list has nothing, wrong data type
        # Match: hashset, int manipulation 
        
        # find shorter list
        if len(arr1) < len(arr2): 
            arr1, arr2 = arr2, arr1

        prefix_set = set()
        
        # create all possible prefixes in arr1
        for num in arr1: 
            # while num is not yet declared a prefix & not cut down to 0 
            while num not in prefix_set and num > 0:
                prefix_set.add(num)
                # remove last digit 123 --> 12
                num = num // 10
        
            # arr1 = [123, 20]
            # prefix_set = [123, 12, 1, 20, 2]

        longest_prefix = 0 
        # check each num in arr2 for longest prefi
        for num in arr2:
            # this num doesn't have matching prefix 
            while num not in prefix_set and num > 0: 
                # reduce num 
                num = num // 10
            # yay! found prefix
            if num in prefix_set: 
                # get max len
                longest_prefix = max(longest_prefix, len(str(num)))
            # 17? no? -> 1? yea
        return longest_prefix

    # Time C: O(m log10M + n log10N) - log 10 reduces digits & m/n = # of numbers in arr1/arr2
    # Space C: O(m log10M) - prefixes proportional w/ # of digits 

