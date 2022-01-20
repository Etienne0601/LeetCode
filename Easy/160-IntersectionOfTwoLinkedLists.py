# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        m = 0 # number of nodes in listA
        n = 0 # number of nodes in listB
        
        currA = headA
        while currA:
            m += 1
            currA = currA.next
        
        currB = headB
        while currB:
            n += 1
            currB = currB.next
            
        currA = headA
        currB = headB
        
        if m > n:
            for i in range(m - n):
                currA = currA.next
        else:
            for i in range(n - m):
                currB = currB.next
        
        while currA and currB:
            if currA is currB:
                return currA
            currA = currA.next
            currB = currB.next
        
        return None
