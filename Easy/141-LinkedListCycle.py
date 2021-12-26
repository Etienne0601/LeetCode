# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if the LL is empty or if there's one element with no next, then there's no cycle
        if (head is None) or (head.next is None):
            return False
        
        slow = head
        fast = head.next
        while fast and fast.next:
            # if slow and fast pointers point to the same node, then there's a cycle
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        # if fast reached the end of the LL without finding a cycle, then return false
        return False
