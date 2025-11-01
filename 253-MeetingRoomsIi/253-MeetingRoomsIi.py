# Last updated: 11/1/2025, 4:59:16 PM
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Understand: given list of intervals w guarenteed start < end times, 
        # return min num of days where you can schedule all with no overlaps
        # input: list of interval objects 
        # output: num 

        # len(intervals) == 1 -> return 1
        # is intervals sorted? 

        # Match: list traversal, accumulator, arrays, two pointer

        # Plan 
        # if end <= start -> nothing 
        # if end > start -> day+=1

        # create start & end array
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])

        result = 0
        count = 0

        # 2 pointers
        startPt, endPt = 0, 0

        # start pointer always ends b4 end
        while startPt < len(intervals):
            if start[startPt] < end[endPt]:
                # one meeting happening 
                startPt += 1
                count += 1
            else: 
                # one meeting has ended
                endPt += 1 
                count -= 1
            # how many were there at max
            result = max(result, count)

        return result

        # Time C: O(nlogn) for sorting through
        # Space C: O(n) for n size input array 
        