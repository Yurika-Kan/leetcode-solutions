# Last updated: 11/4/2025, 11:12:54 AM
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Understand: given a source of truth string word and a abbreviation string word, return whether abbreviation is correct with length of letters replaced 
        # criteria: 
        # no leading 0, no twin numbers, 0

        # "a" -> "a" or "1"
        # word = word -> true 
        
        # Match: two pointer at word & abbr, str traversal 
        # everytime i encounter # at abbr, find the whole int by looping until i hit a letter/ end
        # use that int to step through word 
        # check if p @ word = p @ abbr
        # until traversed 

        wPtr = 0 
        aPtr = 0 

        # traverse... if not match then continue going until they do 
        abbrInt = ""
        increment = 0

        # while both pointers inbounds
        while wPtr < len(word) and aPtr < len(abbr): 
            if word[wPtr] == abbr[aPtr]: 
                wPtr += 1 
                aPtr += 1 
            # if they are not equal bc its a differing letter or a leading 0? --> false
            elif abbr[aPtr].isalpha() or abbr[aPtr] == '0':
                return False
            # ok its a valid abbr letter + digit pair
            else: 
                # accumulate int strings until hit letter or end of word
                while aPtr < len(abbr) and not abbr[aPtr].isalpha(): 
                    abbrInt += abbr[aPtr]
                    aPtr += 1
                # incrementally build digit by digit & intify
                wPtr += int(abbrInt)
                # reset for next use 
                abbrInt = ""
        # at end, are both pointers ending at right after words 
        return wPtr == len(word) and aPtr == len(abbr)

    # Time C: O(n + m) where n is len of word & m is len of abbr
    # Space C: O(1)
