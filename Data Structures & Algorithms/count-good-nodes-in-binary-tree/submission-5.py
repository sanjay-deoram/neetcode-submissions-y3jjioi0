# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,count,max_num):
            if not node:
                return None,0, max_num
            curr_count = 0
            if node.val >=max_num:
                curr_count=1
                max_num = node.val
            
            left = dfs(node.left, curr_count,max_num)
            right = dfs(node.right,curr_count, max_num)
            return node,curr_count + left[1] + right[1], max_num
    
        return dfs(root,0,root.val)[1]