# Last updated: 3/23/2026, 1:24:19 PM
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # check if every letter in ransomNote is in magazine
        # loop through ransomNote and check for each letter in magazine
        # false if not in magazine 
        # if in magazine, remove 
        # true when ransomNote is looped through
        newstr = magazine
        for letter in ransomNote: 
            if letter in newstr: 
                newstr = newstr.replace(letter, "", 1)
            else: 
                return False
        return True




        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        