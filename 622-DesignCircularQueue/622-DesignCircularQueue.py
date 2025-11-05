# Last updated: 11/4/2025, 7:07:00 PM
# Understand: given inputs to functions, implement a queue where the end is the start without built in queue

# edge cases: 
# what if k is 0
# what if invalid params - -#, not int

# Match: doubly linked list - prev & next are dummy front & backs for queue
class ListNode: 
    def __init__(self, val, nxt, prev): 
        self.val = val
        self.nxt = nxt
        self.prev = prev 

class MyCircularQueue:

    def __init__(self, k: int):
        self.limit = k
        # initialize doubly linked list 
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.nxt = self.right


    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        curr = ListNode(value, self.right, self.right.prev)
        # node left of curr - update to include 
        self.right.prev.nxt = curr 
        self.right.prev = curr

        # update space
        self.limit -= 1 
        return True
        
    def deQueue(self) -> bool:
        if self.isEmpty(): 
            return False
        self.left.nxt = self.left.nxt.nxt
        self.left.nxt.prev = self.left
        self.limit +=1
        return True

    def Front(self) -> int:
        if self.isEmpty(): 
            return -1
        return self.left.nxt.val

    def Rear(self) -> int:
        if self.isEmpty(): 
            return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.nxt == self.right

    def isFull(self) -> bool:
        return self.limit == 0

# Time C: O(n) to initialize 
# Space C: O(n)

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
'''
Match: brute force 
    def __init__(self, k: int):
        self.queue = []
        self.limit = k

    def enQueue(self, value: int) -> bool:
        if len(self.queue) >= self.limit: 
            return False
        self.queue.append(value)
        print(self.queue)
        return True
        
    def deQueue(self) -> bool:
        if not self.queue: 
            return False
        # end is beginning
        self.queue.remove(self.queue[0]) -> O(n)
        print(self.queue)
        return True

    def Front(self) -> int:
        if not self.queue: 
            return -1
        return self.queue[0]

    def Rear(self) -> int:
        if not self.queue: 
            return -1
        return self.queue[-1]

    def isEmpty(self) -> bool:
        return not self.queue

    def isFull(self) -> bool:
        if self.queue: 
            return True
        return False

# Time C: O(1) for all except O(n) for dequeue
# Space C: O(n) where n is len of queue

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
'''