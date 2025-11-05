# Last updated: 11/5/2025, 1:54:21 PM
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    # Understand: given a list of x, y points, return boolean if slope is all the same
    # edge cases: 
    # num can be neg
    # Match: Y2-Y1 / X2 -X1 - false if i.slope != j.slope

        # get first two - source of truth slope
        (x1, y1), (x2, y2) = coordinates[:2]
     
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if((y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1)):
                return False
        return True
    
    # Time C: O(n)
    # Space C: O(1)