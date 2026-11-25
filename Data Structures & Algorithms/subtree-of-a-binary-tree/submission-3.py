# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        stack=[(root,subRoot)]
        while stack:
            (r,sR)=stack.pop()
            if self.isSameTree(r,sR):
                return True
            if r.left:
                stack.append((r.left,sR))
            if r.right:
                stack.append((r.right,sR))
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack=[(p,q)]
        while stack:
            p,q=stack.pop()
            if not p and not q:
                continue
            if not (p and q) or p.val!=q.val:
                return False
            stack.append((p.left,q.left))
            stack.append((p.right,q.right))
        return True