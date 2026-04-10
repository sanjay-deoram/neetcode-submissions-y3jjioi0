# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([])
        levels = []

        if root:
            levels.append([root.val])
            q.append(root)
        

        while len(q)>0:
            level=[]
            for i in range(len(q)):
                curr = q.popleft()
                print(curr.val,i)
                if curr.left:
                    level.append(curr.left.val)
                    q.append(curr.left)
                if curr.right:
                    level.append(curr.right.val)
                    q.append(curr.right)
            if level:
                levels.append(level)
        return levels