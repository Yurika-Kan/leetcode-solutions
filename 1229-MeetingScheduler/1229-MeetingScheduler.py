# Last updated: 11/2/2025, 4:52:58 AM
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        # Understand: given two ordered lists (sorted?) & duration num, return earliest start & end time of duration long slot that works for both 
        # are the lists sorted?
        # two pointer
        # edge: 
        
        # Match: two pointers
        # l = slot 1
        # r = slot 2 - a 
        # choose larger start time, check if large - large+duration exists in slot 2 
        # yes -> return that slot
        # no -> push r = slot 2 - b 

        # Match: heap - orders it by min - efficently deals with sorting/choosing slots
        # crucial: intervals < duration = invalid 
        # combine & filter time slots - slots1 + slots 2, filter for range >= durations
        combine = slots1 + slots2

        # note: filter returns filter object -> turn into list 
        slots = list(filter(lambda slot: slot[1] - slot[0] >= duration, combine))
        
        # min heap
        heapq.heapify(slots)

        # loop through, popping & comparing top two if intersection is duration valid
        # while we can still have slots 
        while len(slots) > 1: 
        # popping ensures that comparison is with next earliest interval 
        # end time of earlier slot greater than start + duration of the next earliest slot
        # after pop, heap rebalances automatically so s[0] always points to new smallest element (next earliest slot)
            # [(0,10), (5,20)] 
            # 10 >= 5 + 8?
            if heapq.heappop(slots)[1] >= slots[0][0] + duration: 
                return [slots[0][0], slots[0][0] + duration]
        # return duration valid slot or empty  
        return []

        # Time C: O(nlogn) 
        # Space C: O(n + m) where n is len of slots1, m is len of slots2


    

