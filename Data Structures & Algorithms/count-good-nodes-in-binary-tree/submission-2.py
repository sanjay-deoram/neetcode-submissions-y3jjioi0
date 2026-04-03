class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(node, max_num):
            nonlocal count
            if not node:
                return
            
            # Check if current node is good
            if node.val >= max_num:
                count += 1
                max_num = node.val  # Update max_num for this path
            
            # Always explore both subtrees
            dfs(node.left, max_num)
            dfs(node.right, max_num)

        dfs(root, root.val)
        return count