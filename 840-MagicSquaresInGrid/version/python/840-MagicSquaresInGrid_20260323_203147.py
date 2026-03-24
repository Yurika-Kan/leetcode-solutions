# Last updated: 3/23/2026, 8:31:47 PM
1class Solution:
2    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
3        # U: 
4        # 3x3, distinct s from 1-9
5        # M: DFS
6
7        # r = r - 2 -> 3 rows 
8        # c = c - 2 -> 3 columns
9
10        rows = len(grid)
11        cols = len(grid[0])
12
13        # given top left coordinate
14        def magic(ro, co):
15            # ensure 1 - 9 in ro & co
16            values = set()
17            for i in range(ro, ro + 3): # row -> row + 1, row + 2 (row + 3 is exclusive)
18                for j in range(co, co + 3):
19                    # if duplicate num/alr seen
20                    if grid[i][j] in values or not (1 <= grid[i][j] <= 9): 
21                        return 0
22                    values.add(grid[i][j])
23            # rows 
24            for i in range(ro, ro + 2):
25                if sum(grid[i][co:co+3]) != 15:
26                    return 0
27            # cols 
28            for j in range(co, co + 2): 
29                if (grid[ro][j] + grid[ro+1][j]+ grid[ro+2][j]) != 15:
30                    return 0
31            # diagonals
32            if (grid[ro][co] + grid[ro+1][co+1] + grid[ro+2][co+2] != 15 or 
33            grid[ro][co+2] + grid[ro+1][co+1] + grid[ro+2][co] != 15):
34                return 0
35            return 1
36        
37        magicGrid = 0
38
39        for ro in range(rows - 2): 
40            for co in range(cols - 2): 
41                 magicGrid += magic(ro, co)
42        
43        return magicGrid
44
45        # Time: O(r + c)
46        # Space: O()
47        