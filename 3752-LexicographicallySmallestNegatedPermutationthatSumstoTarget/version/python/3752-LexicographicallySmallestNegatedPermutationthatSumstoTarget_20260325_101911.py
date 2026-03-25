# Last updated: 3/25/2026, 10:19:11 AM
1class Solution:
2    # sum of permutation array of size n = sum of all # up to N
3    def sumN(self, n: int) -> int: 
4        return n * (n+1)//2
5
6    def lexSmallestNegatedPerm(self, n: int, target: int) -> List[int]:
7        sumN = self.sumN(n)
8        # target must be in between min & max possible sum of this permutation num list
9        if target < -sumN or target > sumN: 
10            return []
11
12        result = []
13
14        # greedy = largest num first bc they make bigger diff
15        # must have each num in range n->1 - either positive or negative
16        for i in range(n, 0, -1): # 3, 2, 1
17            # can reach target without i => -i
18            # If I choose -i, will I still have enough positive capacity left to hit target
19            if self.sumN(i-1) - i >= target: # 2 = 2 * (2+1) // 2  = 3 
20                # adjust remaining goal ie remove 
21                target += i # choose -i
22                result.append(-i)
23            else:
24                target -= i
25                result.append(i)
26        
27        if target != 0:
28            return []
29
30        result.sort()
31        return result
32
33        # Time: O(n log n) sorting
34        # Space: O(n)
35        