# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        curr = prev = ListNode(next=head)
        isFirst = True
        while curr != None:
            curr = curr.next
            while curr != None and curr.val == val:
                curr = curr.next
            if isFirst:
                head = curr
            prev.next = curr
            prev = prev.next
            isFirst = False
            
        
        return head

