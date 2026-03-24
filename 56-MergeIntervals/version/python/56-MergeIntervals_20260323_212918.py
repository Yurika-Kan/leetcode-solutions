# Last updated: 3/23/2026, 9:29:18 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        # sort based on start val of intervals
4        intervals.sort(key = lambda i : i[0])
5
6        result = [intervals[0]] # initialize
7
8        for start, end in intervals[1:]:
9            # most recent interval's end val
10            lastEnd = result[-1][1]
11
12            # most recent end val overlaps with my start
13            if start <= lastEnd: 
14                # set new last end
15                result[-1][1] = max(lastEnd, end)
16
17            else: 
18                # not overlapping - add to output
19                result.append([start,end])
20        return result
21
22        # Time: O(nlogn) - sort
23        # Space: O(n)