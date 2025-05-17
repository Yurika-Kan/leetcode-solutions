# Last updated: 5/17/2025, 12:54:40 AM
'''
Time Complexity: O(n+m)
Space Complexity: O(1)
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Understand: check if s and t contain same letter makeup
        #Match: freq map 
        #Plan: create freq map for s then t, check if s == t
        #Implement: 
        smakeup = {}
        tmakeup = {}
        for char in s: 
            smakeup[char]=smakeup.get(char, 0)+1
        for char in t: 
            tmakeup[char]=tmakeup.get(char, 0)+1
        return smakeup == tmakeup 
        #Review: 
        # s = '', t = '' --> true 
        # s = '', t = 'a' --> false
        # s = 'ss', t = 's' --> false 
        # s = 'hello', t = 'oellh' --> true
        #Evaluate: O(n+m)
        