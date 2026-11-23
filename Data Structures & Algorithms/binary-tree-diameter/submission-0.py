# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia=0
        dep=self.walk(root)
        return max(self.dia,dep)

    def walk(self, root:Optional[TreeNode]) -> int:
        if not root:
            return -1
        l_dep=1+self.walk(root.left)
        r_dep=1+self.walk(root.right)
        print('l',l_dep)
        print('r',r_dep)
        self.dia=max(l_dep+r_dep,self.dia)
        return max(l_dep,r_dep)
        