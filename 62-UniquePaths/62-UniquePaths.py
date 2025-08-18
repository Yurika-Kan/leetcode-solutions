# Last updated: 8/18/2025, 3:18:42 PM
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # U: count unique paths 
        # M: tabulation, 2d dp, memoization
        # P: 
        # base case: first 
        # recurrence relation: right = self[m][n+1], down = self[m+1][n]
        # botto row are all ones 
        row =[1] * n

        # make new row
        for i in range(m-1):
            # make a row for each, set all to one, last index of each row is always 1
            # beginning point & initalized row
            newRow = [1] * n
            # traverse from second to last, keep going till beginning, go backwards 
            # index in each row, avoid out of bounds 
            for j in range (n-2, -1, -1):
                # add right & bottom
                newRow[j] = newRow[j+1] + row[j]
            # update row
            row = newRow
        # first value
        return row[0]

# Time Complexity: O(m * n)
# Space Complexity: O(n)