# Last updated: 3/23/2026, 1:24:29 PM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # U: find longest starting letters of words in list
        # M: hashmap - each word w letter count, compare with shortest word's each letter freq
        # trie - prefix 

        result = ""

        # for each string, check against first word
        for i in range(len(strs[0])):
            for stri in strs:
                # if at end & prefix is done / overflows 
                # if this string at i is diff than any stri at i
                if i == len(stri) or stri[i] != strs[0][i]:
                    # prefix done boom
                    return result
            result = result + stri[i]
        
        return result

        # Time: O(n)
        # Space: O(n)