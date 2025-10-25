# Last updated: 10/25/2025, 3:13:50 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Understand: given head of linked list, return if there is cycle
        # input: head of linked list 
        # output: boolean 

        # Match: visited set / list / bool 

        # edge: 
        # one node -> false 
        if not head: 
            return False 

        # how to identify the node？ like what if there are 2 nodes with the same value - location？ 
        visited = set()
        curr = head 
        # try to find cycle or until fully through list 
        while curr: 
            if curr.next in visited: 
                return True
            else: 
                curr = curr.next
                visited.add(curr)
        return False

    # Time C: O(n)
    # Space C: O(n)