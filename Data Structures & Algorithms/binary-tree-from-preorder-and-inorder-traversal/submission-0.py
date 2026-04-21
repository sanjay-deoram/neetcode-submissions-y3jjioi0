class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {value: idx for idx, value in enumerate(inorder)}
        self.pre_index = 0
        def dfs(l, r):
            if l > r:
                return None
            root_val = preorder[self.pre_index]
            self.pre_index += 1
            root = TreeNode(root_val)
            mid = index_map[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root
        return dfs(0, len(preorder) - 1)