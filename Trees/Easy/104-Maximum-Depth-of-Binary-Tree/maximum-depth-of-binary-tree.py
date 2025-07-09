# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = []  # Use a queue to perform BFS (Breadth-First Search)

        if not root:
            return 0  # Base case: if the tree is empty, return 0

        count = 0  # This will keep track of the depth

        q.append(root)  # Start by adding the root node to the queue

        while q:  # While there are nodes to process
            level_size = len(q)  # Get the number of nodes in the current level
            for i in range(level_size):  # Process all nodes in the current level
                cur = q.pop(0)  # Pop the front node
                if cur.left:
                    q.append(cur.left)  # Add left child to the queue
                if cur.right:
                    q.append(cur.right)  # Add right child to the queue
            count += 1  # One level is finished, increment depth

        return count  # Return the total depth
