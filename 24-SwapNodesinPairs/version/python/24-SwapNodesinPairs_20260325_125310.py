# Last updated: 3/25/2026, 12:53:10 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode(0, head)
9        prev = dummy
10        curr = head 
11
12        while curr and curr.next: 
13            # save pointers
14            nxtPair = curr.next.next
15            second = curr.next 
16
17            # reverse pair
18            second.next = curr 
19            curr.next = nxtPair
20            prev.next = second
21
22            # update pointers
23            prev = curr
24            curr = nxtPair
25
26        return dummy.next
27
28        # Time: O(n)
29        # Space: O(1)
30        