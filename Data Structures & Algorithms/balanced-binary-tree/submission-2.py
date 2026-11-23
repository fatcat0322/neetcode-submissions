# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bal=True
        self.height(root)
        return self.bal

    def height(self, root: Optional[TreeNode]) -> int:
        if not root or not self.bal:
            return 0
        l_dep=self.height(root.left)
        r_dep=self.height(root.right)
        if abs(l_dep-r_dep)>1:
            self.bal=False
        return 1+max(l_dep,r_dep)