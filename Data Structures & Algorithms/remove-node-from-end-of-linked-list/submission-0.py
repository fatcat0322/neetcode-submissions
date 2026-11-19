# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum=ListNode()
        dum.next=head
        ptr1=ptr2=dum
        for i in range(n):
            ptr2=ptr2.next
        while ptr2:
            prev=ptr1
            ptr1=ptr1.next
            ptr2=ptr2.next
        prev.next=prev.next.next
        return dum.next
    