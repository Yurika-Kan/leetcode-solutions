# Last updated: 11/1/2025, 4:59:18 PM
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # U: find connected adjacent 1's from list of list 
        # M: dfs/bfs, recursive, grid
        # P: find 1, run dfs & count  valid ones
        #horizontally & vertically = row + - 1, column + - 1

        # empty grid - return 0 
        if not grid: 
            return 0

        # initialize
        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add((r, c))
            q.append((r,c))
            
            while q: 
                # expand island
                # bfs: pop the first element 
                # dfs: pop the last, non recursively
                row, col = q.popleft()
                # right, left, top, bottom
                directions= [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions: 
                    r, c = row + dr, col + dc
                    # inside grid, valid island, unvisited
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit: 
                        # add to queue to continue bfs-ing 
                        q.append((r, c))
                        # mark visited 
                        visit.add((r, c))

        for r in range(rows): 
            for c in range(cols):
                # new island 
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c) 
                    islands +=1
        return islands
     
        # Time Complexity: O(m*n) where m is the rows, n is the columns
        # Space Complexity: O(m*n)