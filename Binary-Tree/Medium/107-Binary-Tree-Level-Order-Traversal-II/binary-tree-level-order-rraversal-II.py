# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val  # Store the value of the node
#         self.left = left  # Pointer to the left child
#         self.right = right  # Pointer to the right child

from collections import deque  # Import deque for efficient queue operations

class Solution:
   def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
       if not root:
           return []  # Edge case: If the tree is empty, return an empty list

       q = deque()  # Initialize a queue to store nodes for level-order traversal
       q.append(root)  # Start with the root node
       ans = []  # List to store the result

       while q:
           temp = []  # Temporary list to store the current level nodes' values
           level_order = len(q)  # Number of nodes at the current level

           for i in range(level_order):  # Process each node in the current level
                cur = q.popleft()  # Remove the front node from the queue
                temp.append(cur.val)  # Store its value

                if cur.left:
                   q.append(cur.left)  # Add the left child to the queue if it exists
                if cur.right:
                   q.append(cur.right)  # Add the right child to the queue if it exists

           if temp:
               ans.append(temp)  # Add the current level values to the result list
               
       return list(reversed(ans))  # Reverse the result to get bottom-up order
