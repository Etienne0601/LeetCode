# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # first use the tortoise and the hare algorithm to get
        # a pointer to the midpoint of the linked list
        slow = head
        fast = head
        
        while fast != None and fast.next != None:
            # move slow along once and fast along twice
            slow = slow.next
            fast = fast.next.next
        
        # save the midpoint
        midpoint = slow
        
        # now reverse the second half of the linked list
        prev = None
        while slow != None:
            
