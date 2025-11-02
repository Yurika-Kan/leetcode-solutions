# Last updated: 11/2/2025, 4:57:00 AM
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # array
        self.minHeap = nums
        self.k = k
        # make into min heap 
        heapq.heapify(self.minHeap)
        # only need to know largest k vals 
        # initialize size 
        while len(self.minHeap) > k: 
            heapq.heappop(self.minHeap)
            
        # if heap has less than k elements

    def add(self, val: int) -> int:
        # add new val to heap 
        heapq.heappush(self.minHeap, val)
        # maintain size 
        if len(self.minHeap) > self.k:
            # remove new k + 1 smallest 
            heapq.heappop(self.minHeap)
        # first is smallest val 
        return self.minHeap[0]
        # min heap - add & pop - O(n)
        # if size > k, remove smallest from heap
        # while size of heap > k, pop min # 
        # return min - O(1)

    # Time Complexity: O(mlogk) where m is # of times add() is called & k is k
    # Space Complexity: O(1)
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)