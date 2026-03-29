# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left,key)
        else:
            # Check for 0-1 children
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # We know it has leaf children now, find the smallest val
            curr = root.right

            while curr and curr.left:
                curr = curr.left
            
            # replace the root with the value so we dont disconnect the tree, then call the deleteNode to remove the value from the tree.
            root.val = curr.val
            root.right = self.deleteNode(root.right,curr.val)
        return root

