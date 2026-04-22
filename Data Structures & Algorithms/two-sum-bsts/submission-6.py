# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.numbers = set()
        self.found = False
        def dfs(node):
            if not node:
                return 
            self.numbers.add(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root1)

        def dfs2(node2):
            if not node2:
                return 
            
            if target - node2.val in self.numbers:
                print('found')
                self.found = True
                return
            
            dfs2(node2.left)
            dfs2(node2.right)
        dfs2(root2)
        
        return self.found