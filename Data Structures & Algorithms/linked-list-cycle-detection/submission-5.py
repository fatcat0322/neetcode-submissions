# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast=head.next
        slow=head
        while fast is not slow:
            print(fast.val,slow.val)
            if fast.next and fast.next.next:
                fast=fast.next.next
                print('new fast',fast.val)
            else:
                return False
            slow=slow.next
        return True
