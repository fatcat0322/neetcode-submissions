# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lar,sml=(p.val,q.val) if p.val>q.val else (q.val,p.val)
        cur=root
        while True:
            if cur.val>lar:
                cur=cur.left
            elif cur.val<sml:
                cur=cur.right
            elif cur.val>=sml and cur.val<=lar:
                return cur