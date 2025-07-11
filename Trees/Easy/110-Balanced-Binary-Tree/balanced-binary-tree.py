# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Main function to check if the tree is height-balanced

        def dfs(root):
            if not root:
                return [True, 0]  # Base case: empty tree is balanced and has height 0

            left = dfs(root.left)  # Recursively check left subtree
            right = dfs(root.right)  # Recursively check right subtree
            isbal = left[0] and right[0] and abs(left[1]-right[1]) <= 1  
            # Tree is balanced if both subtrees are balanced and height difference <= 1

            return [isbal, 1 + max(left[1], right[1])]  
            # Return [isBalanced, height] for this node

        return dfs(root)[0]  # Return whether the entire tree is balanced
