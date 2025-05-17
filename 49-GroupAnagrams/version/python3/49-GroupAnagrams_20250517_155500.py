# Last updated: 5/17/2025, 3:55:00 PM
'''
Time Complexity: O(n*k log k)
Space Complexity: O(n*k)
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize freq map         
        # iterate through strs:
        # if sorted not in freq map key, add it and append to empty value list
        # else if in, append to the value list 
        # return each value of map in list 
        freqMap = {}
        for s in strs: 
            # sorted makes the string into a list!!! --> convert it back to a str 
            word = ''.join(sorted(s))
            if word not in freqMap:
                freqMap[word] = [s]
            else: 
                freqMap[word].append(s)
        return list(freqMap.values())