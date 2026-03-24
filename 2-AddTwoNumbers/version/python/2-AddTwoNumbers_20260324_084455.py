# Last updated: 3/24/2026, 8:44:55 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
9        dummy = ListNode()
10        # points to where we insert new digit
11        curr = dummy 
12
13        carry = 0 # to maintain
14
15        # while either is not null
16        # while carry exists - carry edge case for carry over when both nodes dont have next node & remembers prev loop carry
17        while l1 or l2 or carry: 
18            if l1: # not empty
19                val1 = l1.val 
20            else: 
21                val1 = 0
22            if l2:
23                val2 = l2.val
24            else:
25                val2 = 0
26            
27            # computer new digit 
28            val = val1 + val2 + carry
29        
30            # digit if carry over 
31            carry = val // 10 # 9 // 10 => 0 but 12 // 10 => 1
32            # mod = remainder = this digit 
33            val = val % 10 # 9 % 10 = 0 but 12 % 10 => 2
34
35            curr.next = ListNode(val)
36
37            # update ptrs 
38            curr = curr.next 
39            l1 = l1.next if l1 else None
40            l2 = l2.next if l2 else None
41
42        return dummy.next
43
44        # Time: O(n + m)
45        # Space: O(1)