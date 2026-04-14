class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                return False

            left = valid(node.left, left, node.val)
            right = valid(
                node.right, node.val, right
            )
            return left and right 

        return valid(root, float("-inf"), float("inf"))