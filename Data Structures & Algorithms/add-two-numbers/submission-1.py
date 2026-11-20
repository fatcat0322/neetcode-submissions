# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode()
        tail=dum
        ten=False
        while l1 and l2:
            if ten:
                val=l1.val+l2.val+1
            else:
                val=l1.val+l2.val
            ten=val>9
            val%=10
            tailn=ListNode(val)
            tail.next=tailn
            tail=tail.next
            l1=l1.next
            l2=l2.next
        l=l1 if l1 else l2
        while l:
            if ten:
                val=l.val+1
            else:
                val=l.val
            ten=val>9
            val%=10
            tailn=ListNode(val)
            tail.next=tailn
            tail=tail.next
            l=l.next
        if ten:
            tailn=ListNode(1)
            tail.next=tailn
        return dum.next
        