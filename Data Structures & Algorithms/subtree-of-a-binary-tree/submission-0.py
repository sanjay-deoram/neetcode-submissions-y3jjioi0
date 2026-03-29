# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if self.isSameTree(root,subRoot):
            return True
        found_in_left = self.isSubtree(root.left, subRoot)
        found_in_right = self.isSubtree(root.right, subRoot)
        return found_in_left or found_in_right

    def isSameTree(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        
        left = self.isSameTree(p.left,q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right