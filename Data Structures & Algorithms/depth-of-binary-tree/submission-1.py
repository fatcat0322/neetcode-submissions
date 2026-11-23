# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack=[(1,root)] if root else []
        max_depth=0
        while stack:
            depth,cur=stack.pop()
            max_depth=max(max_depth,depth)
            if not cur.left and not cur.right:
                continue
            depth+=1
            if cur.left:
                stack.append((depth,cur.left))
            if cur.right:
                stack.append((depth,cur.right))
        return max_depth
        