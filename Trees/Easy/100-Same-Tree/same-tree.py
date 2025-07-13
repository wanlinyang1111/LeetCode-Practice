# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both trees are empty, they are the same
        if not p and not q:
            return True
        
        # If one is None and the other is not, they are different
        if not p or not q:
            return False

        # If current nodes' values are equal, check left and right subtrees recursively
        if p.val == q.val:
            return (self.isSameTree(p.left, q.left) and
                    self.isSameTree(p.right, q.right))
        
        # If values are different, return False
        else:
            return False
