class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        t1 = set()
        found = False

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            t1.add(node.val)
            dfs(node.right)

        dfs(root1)

        def dfs2(node):
            nonlocal found
            if node is None:
                return
            
            dfs2(node.left)
            
            if target - node.val in t1:
                found = True
            
            dfs2(node.right)

        dfs2(root2)

        return found