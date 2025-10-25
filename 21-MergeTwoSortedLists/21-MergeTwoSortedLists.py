# Last updated: 10/25/2025, 2:41:39 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    # Understand: given 2 sorted linked lists, merge and output merged list head
    # input: 2 ListNode objects
    # output: 1 ListNode object 

        # edge: empty node? no next --> return other ll
        
        if not list1: 
            return list2 
        if not list2: 
            return list1

        # Match: linked list, comparing with 2 pointer, dummy head

        # dummy head 
        prehead = ListNode()
        tail = prehead

        # stop lists end
        while list1 and list2: 
            if list1.val < list2.val: 
                # smaller num 
                tail.next = list1
                # point to next index
                list1 = list1.next
            else: 
                tail.next = list2
                list2 = list2.next
            # either way, move the tail end to contiually add to end 
            tail = tail.next
        
        # add up the rest if there are still nodes left
        tail.next = list1 or list2

        # dummy's next = head of our list
        return prehead.next

    # Time C: O(n+m) n, m = len(list1), len(list2)
    # Space C: O(1)
