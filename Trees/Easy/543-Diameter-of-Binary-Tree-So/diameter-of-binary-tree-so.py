# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        self.res = 0  # Initialize global result to store the max diameter

        # Helper function to calculate height of the tree
        def dfs(root):
            if not root:
                return 0  # Base case: height of null node is 0

            left = dfs(root.left)    # Recursively calculate height of left subtree
            right = dfs(root.right)  # Recursively calculate height of right subtree

            # Update the diameter at the current node
            self.res = max(self.res, left + right)

            # Return the height of the current node
            return 1 + max(left, right)

        dfs(root)  # Start DFS traversal from the root
        return self.res  # Return the maximum diameter found
