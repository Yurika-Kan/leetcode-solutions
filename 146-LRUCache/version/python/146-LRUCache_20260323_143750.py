# Last updated: 3/23/2026, 2:37:50 PM
1class Node: 
2    # dummy LRU & MRU
3    def __init__(self, key, val):
4        self.key, self.val = key, val
5        self.prev = None
6        self.next = None
7
8class LRUCache:
9
10    def __init__(self, capacity: int):
11        self.capacity = capacity
12        self.cache = {} # map key to node
13
14        # dummy nodes
15        self.left, self.right = Node(0, 0), Node(0,0)
16        # connect pointers
17        self.left.next, self.right.prev = self.right, self.left
18
19    
20    # helper functions - pointer 
21    # self right & next are dummy pointers at ends! 
22
23    # remove node from left 
24    def remove(self, node): 
25        prev = node.prev
26        next = node.next
27        # my prev next is my next - bye me
28        prev.next = next   # left neighbor now skips over node
29        next.prev = prev   # right neighbor now skips back over node
30    # Before:  [prev] <-> [node] <-> [next]
31    # After:   [prev] <-----------> [next]  
32
33
34    # insert node at right with dummy empty next
35    def insert(self, node):
36        prev = self.right.prev   # whoever was last before the right dummy
37        prev.next = node         # that node now points forward to new node
38        node.prev = prev         # new node points back to it
39        node.next = self.right   # new node points forward to right dummy
40        self.right.prev = node   # right dummy points back to new node
41        # Before:  [prev] <-> [node] <-> [next]
42        # After:   [prev] <-> [node] <-> [new] <-> [next] 
43        
44
45    # return key's value, -1 if dne
46    def get(self, key: int) -> int:
47        if key in self.cache: 
48            # update for status
49            self.remove(self.cache[key])
50            self.insert(self.cache[key])
51            return self.cache[key].val
52        return -1
53    
54    # update key's value or add new pair to cache if dne
55    # if cache exceeds its capacity remove least recently used key (ie get / used operation called) 
56    def put(self, key: int, value: int) -> None:
57        if key in self.cache: 
58            self.remove(self.cache[key])
59        self.cache[key] = Node(key, value)
60        self.insert(self.cache[key])
61
62        if len(self.cache) > self.capacity: 
63            lru = self.left.next 
64            self.remove(lru)
65            # remove lru
66            del self.cache[lru.key]
67        
68# fifo - queue 
69# hash map
70
71# Time: O(1) for put & get
72# Space: O(n)
73        
74
75
76# Your LRUCache object will be instantiated and called as such:
77# obj = LRUCache(capacity)
78# param_1 = obj.get(key)
79# obj.put(key,value)