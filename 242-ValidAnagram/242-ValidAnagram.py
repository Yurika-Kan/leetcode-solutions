# Last updated: 5/18/2025, 2:20:26 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check if s and t contain same letter makeup
        #create freq map for s then t, check if s == t
        smakeup = {}
        tmakeup = {}
        for char in s: 
            # get curr count or default 0 to increment
            smakeup[char]=smakeup.get(char, 0)+1
        for char in t: 
            tmakeup[char]=tmakeup.get(char, 0)+1
        return smakeup == tmakeup 

        # s = '', t = '' --> true 
        # s = '', t = 'a' --> false
        # s = 'ss', t = 's' --> false 
        # s = 'hello', t = 'oellh' --> true

        # Time Complexity: O(n+m)
        # Space Complexity: O(n+m)
        