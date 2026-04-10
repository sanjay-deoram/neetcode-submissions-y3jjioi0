class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, count,max_num):
            if not node:
                return None, 0, max_num
            
            current_count = 0
            if node.val >=max_num:
                current_count = 1
                max_num = node.val
            
            left = dfs(node.left,count,max_num)
            right = dfs(node.right, count,max_num)
            return node, current_count + left[1] + right[1], max_num
        return dfs(root,0,root.val)[1]