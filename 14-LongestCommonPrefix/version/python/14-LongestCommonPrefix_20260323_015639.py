# Last updated: 3/23/2026, 1:56:39 AM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        # U: find longest starting letters of words in list
4        # M: hashmap - each word w letter count, compare with shortest word's each letter freq
5        # trie - prefix 
6
7        result = ""
8
9        # for each string, check against first word
10        for i in range(len(strs[0])):
11            for stri in strs:
12                # if at end & prefix is done / overflows 
13                # if this string at i is diff than any stri at i
14                if i == len(stri) or stri[i] != strs[0][i]:
15                    # prefix done boom
16                    return result
17            result = result + stri[i]
18        
19        return result
20
21        # Time: O(n)
22        # Space: O(n)