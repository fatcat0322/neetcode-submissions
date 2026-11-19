# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast=slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        bw_cur=slow.next
        slow.next=None
        bw_prev=None
        while bw_cur:
            bw_nxt=bw_cur.next
            bw_cur.next=bw_prev
            bw_prev=bw_cur
            bw_cur=bw_nxt
        first=head
        second=bw_prev
        while second:
            nxt_1=first.next
            nxt_2=second.next
            first.next=second
            second.next=nxt_1
            first=nxt_1
            second=nxt_2