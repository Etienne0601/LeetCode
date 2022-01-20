# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currA = headA
        currB = headB
        
        # currA walks through listA and then listB,
        # while currB walks thorugh listB and then listA
        while True:
            if currA is currB:
                return currA
            
            if currA is None:
                # currA == None and currB != None
                currA = headB
                currB = currB.next
            else:
                # currA != None
                if currB is None:
                    # currA != None and currB == None
                    currB = headA
                else:
                    # currA != None and currB != None
                    currB = currB.next
                currA = currA.next
