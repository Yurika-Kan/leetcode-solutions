# Last updated: 10/11/2025, 2:56:48 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        # Understand: given a string, parse through to return a number 
        # Match: hashmap, compare curr w next
        # Plan: left -> right, boolean for i, x, c
        # if curr num < next num -> -
        # if curr num > next num -> +

        # hashmap O(7)
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100, 
            'D': 500, 
            'M': 1000
        }

        result = 0 
        #IVM 
        #len = 3
        for i in range(len(s)):
            # check if next index in bounds - 
            # condition: must have next & must be curr < next -> add
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]: 
                result -= roman[s[i]]
            else: 
            # condition: add 
                result += roman[s[i]]
        return result
        
        # Time C: O(n)
        # Space C: O(1)