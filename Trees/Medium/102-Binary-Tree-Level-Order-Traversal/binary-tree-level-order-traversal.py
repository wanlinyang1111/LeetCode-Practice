# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
This algorithm performs a level order traversal of a binary tree.
It uses a queue (deque) to process nodes level by level.

1. Initialize a queue and append the root node.
2. Use a while loop to process nodes until the queue is empty.
3. For each level, determine the number of nodes at that level.
4. Use a for loop to process all nodes at the current level:
   - Pop the first node from the queue.
   - Store its value in a temporary list.
   - Append its left and right children (if they exist) to the queue.
5. Append the temporary list to the final answer list.
6. Return the answer list containing level-wise node values.
'''

from collections import deque  # Import deque for efficient queue operations

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:  # If the tree is empty, return an empty list
            return []

        q = deque()  # Initialize the queue
        q.append(root)  # Add the root node to the queue

        ans = []  # List to store the final result

        while q:  # While there are nodes in the queue
            level_size = len(q)  # Get the number of nodes at the current level
            temp = []  # Temporary list to store values of the current level

            for i in range(level_size):  # Process each node in the current level
                cur = q.popleft()  # Remove and get the first node from the queue
                temp.append(cur.val)  # Store the node's value

                if cur.left:  # If the node has a left child, add it to the queue
                    q.append(cur.left)
                if cur.right:  # If the node has a right child, add it to the queue
                    q.append(cur.right)

            if temp:  # If the temporary list contains values, add it to the final result
                ans.append(temp)
        
        return ans  # Return the list of level order values
