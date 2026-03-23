# Last updated: 3/23/2026, 1:24:20 PM
class Solution(object):
    def firstUniqChar(self, s):
        # find first original character 
        # traverse through the word char by char 
        # if char counter in word is one 
        freq = {}

        for char in s: 
            if char in freq: 
                freq[char] += 1
            else: 
                freq[char] = 1

        if freq.items() == 0: 
            return -1

        for index, char in enumerate(s): 
            if freq[char] == 1: 
                return index
        return -1
        
        # return char 
        # else continue traversing until end
        # outside of loop return -1 
        """
        :type s: str
        :rtype: int
        """
        