class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_num):
            nonlocal count
            if not node:
                return 0
            if node.val >= max_num:
                count += 1
                max_num = node.val
            dfs(node.left, max_num)
            dfs(node.right, max_num)
        dfs(root, root.val)
        return count