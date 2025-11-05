# Last updated: 11/4/2025, 8:16:33 PM
class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        # Understand: given a list of lists, return the indexes of list items that are not subsets of other list items
        # input: [[]]
        # output: [ints]

        # edge: 
        # len(favoriteCompanies) = 1 -> 0

        # Match: hashmap, separate by "buckets" - every entry is distinct - no need to compare same length ons
        # Plan: 
        res = []
        # attach index to each set
        indexed = [(idx, set(companies)) for idx, companies in enumerate(favoriteCompanies)]

        # sort list by length of each list item
        indexed.sort(key= lambda x:len(x[1]))
        n = len(indexed)

        # for me, check if subset w others
        for i in range(n):
            is_subset = False
            # me vs the rest of the bigger ppl
            for j in range(i+1, n):
                if indexed[i][1].issubset(indexed[j][1]): #O(k) - O(1) * set of size k
                    is_subset = True
                    break
            # no need to check me with rest, im alr out
            # if its not a subset, append to result
            if not is_subset: 
                # add og index
                res.append(indexed[i][0])
        
        return sorted(res)
    
    # Time C: O(n^2)
    # Space C: O(n)