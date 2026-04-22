# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        def found(root2, compliment):
            if not root2:
                return False
            if root2.val == compliment:
                return True
            if root2.val > compliment:
                return found(root2.left, compliment)
            else:
                return found(root2.right, compliment)
            return False

        def dfs(node):
            if not node:
                return False
            
            if found(root2, target-node.val):
                return True
            l = dfs(node.left)
            r = dfs(node.right)
            return l or r
        return dfs(root1) or False