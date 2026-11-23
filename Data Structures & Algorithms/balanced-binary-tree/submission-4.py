# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.height(root)>=0

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_dep=self.height(root.left)
        r_dep=self.height(root.right)
        if l_dep<0 or r_dep<0:
            return -1
        if abs(l_dep-r_dep)>1:
            return -1
        return 1+max(l_dep,r_dep)