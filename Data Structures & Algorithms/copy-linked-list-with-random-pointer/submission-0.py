"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cur=head
        node_dict={None:None}
        while cur:
            n=Node(cur.val)
            node_dict[cur]=n
            cur=cur.next
        cur=head
        while cur:
            node_dict[cur].next=node_dict[cur.next]
            node_dict[cur].random=node_dict[cur.random]
            cur=cur.next
        return node_dict[head]