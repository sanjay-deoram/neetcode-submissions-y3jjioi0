class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found = False
        def dfs(node,target_sum):
            nonlocal found
            if not node:
                return False
            if not node.left and not node.right and node.val == target_sum:
                found = True
                return True

            dfs(node.left, target_sum-node.val)
            dfs(node.right, target_sum-node.val)
        
        dfs(root,targetSum) 
        return found