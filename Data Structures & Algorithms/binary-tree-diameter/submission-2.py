# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        dep=self.depth(root)
        return self.dia

    def depth(self, root:Optional[TreeNode]) -> int:
        if not root:
            return 0
        l_dep=1+self.depth(root.left)
        r_dep=1+self.depth(root.right)
        self.dia=max(l_dep+r_dep-2,self.dia)
        return max(l_dep,r_dep)
        