# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if the LL is empty, then there's no cycle
        if head is None:
            return None
        
        slow = head
        fast = head.next
        
        while slow is not fast:
            # if fast or fast.next are None, then there's no cycle
            if (fast is None) or (fast.next is None):
                return None
            slow = slow.next
            fast = fast.next.next
        
        # at this point we know there is a cycle
        slow = head
        fast = fast.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next
        
        return slow
