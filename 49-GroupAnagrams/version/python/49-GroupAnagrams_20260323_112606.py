# Last updated: 3/23/2026, 11:26:06 AM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        # U: hashmap - 
4        # map charCount to list of anagrams
5        result = defaultdict(list) # what if this dne yet
6
7        for stri in strs: 
8            abcfreq = [0] * 26 # a to z = 0 -> i = 25
9
10            # char count map of string
11            for charac in stri:
12                # ascii val - assume a -> b is always one unit bigger
13                # sets / grounds charac to count[i] -> increment that alphabet letter
14                # 0 = a, 1 = b, 2 = c, 3 = d
15                # 1, 1, 1, 0 = "cab"
16                abcfreq[ord(charac) - ord("a")] += 1
17
18            # for each string, add itself to the abcfreq map in results
19            # result = {
20            # (1, 0, 1, 0, ..., 0, 1, 0, ..., 0): ["act", "cat"],
21            # (0, 0, 0, ..., 0, 1, 1, 0, ..., 0): ["tops", "pots", "stop"],
22            # (1, 0, 0, 0, ..., 0): ["hat"]
23            # }
24            result[tuple(abcfreq)].append(stri)
25
26        # grouped by the same abcfreq char count makeup = anagram
27        return list(result.values())
28
29        #Time: O(m * n) - m is # of strings, n is length of each string
30