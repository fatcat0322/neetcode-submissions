# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack=[(p,q)]
        while stack:
            p_cur,q_cur=stack.pop()
            if not p_cur and not q_cur:
                continue
            if not (p_cur and q_cur) or p_cur.val!=q_cur.val:
                return False
            stack.append((p_cur.left,q_cur.left))
            stack.append((p_cur.right,q_cur.right))
        return True