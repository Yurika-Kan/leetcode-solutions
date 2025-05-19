# Last updated: 5/18/2025, 6:28:26 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # freq map         
        freqMap = {}
        # iterate through strs:
        for s in strs: 
            # sorted makes the string into a list!!! --> convert it back to a str 
            word = ''.join(sorted(s))
            # if sorted not in freq map key, add it and append to empty value list
            if word not in freqMap:
                freqMap[word] = [s]
            # else if in, add og word value to sorted word key  
            else: 
                freqMap[word].append(s)
        # return each value of map in list 
        return list(freqMap.values())

# n - strs 
# k = sorted s
# Time Complexity: O(nklogn)
# Space Complexity: O(n*k)