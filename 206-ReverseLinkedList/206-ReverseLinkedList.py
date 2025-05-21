# Last updated: 5/21/2025, 2:38:15 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 0 -> 1 -> 2 -> 3 
    # 3 -> 2 -> 1 -> 0
    # 0.next = None & prev = 0
    # 1.next = prev & prev = 1
    # 2.next = prev & prev = 2
    # 3.next = prev & prev = 3
    
        current = head 
        prev = None 
        while current: 
            # hold so next val is not lost: 1
            temp = current.next
            # reverse pointer: 1 -> 0
            current.next = prev
            # move on: x -> 1
            prev = current
            # so we are still on track 
            current = temp
        # prev bc current is None after list iteration
        return prev
    
    # Time Complexity: O(n)
    # Space Complexity: O(1)