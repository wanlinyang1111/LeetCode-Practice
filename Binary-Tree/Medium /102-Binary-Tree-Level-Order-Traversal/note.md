# Notes for Problem number 102 - Binary Tree Level Order Traversal

Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/

## Key Concepts
- **The key concept of this problem is Breadth-First Search (BFS) using a queue.**
- **We traverse the tree level by level and store the values in a list.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Forgetting to check if the root is `None`:
- **Error**: Not handling an empty tree correctly.
- **Reason**: If `root` is `None`, the function should return an empty list.
- **How to Avoid**: Add an early return condition: `if not root: return []`.

### 2. Using a list instead of `deque` for the queue:
- **Error**: Using a list for queue operations results in inefficient `pop(0)` operations.
- **Reason**: `list.pop(0)` has O(n) time complexity, while `deque.popleft()` has O(1) complexity.
- **How to Avoid**: Use `collections.deque` for efficient queue operations.

### 3. Not processing all nodes at the current level before moving to the next:
- **Error**: Mixing different levels in the output list.
- **Reason**: If we process nodes without considering level boundaries, the output structure will be incorrect.
- **How to Avoid**: Use `level_size = len(q)` before iterating through the current level.

### 4. Appending `TreeNode` instead of `TreeNode.val` to the result:
- **Error**: Storing `TreeNode` objects instead of integer values in the output list.
- **Reason**: Each level should contain only values, not the `TreeNode` objects themselves.
- **How to Avoid**: Append `cur.val` instead of `cur` in the `temp` list.

### 5. Forgetting to add child nodes to the queue:
- **Error**: Not adding `cur.left` or `cur.right` to the queue results in missing nodes.
- **Reason**: If a child node is not added, it will not be processed in the next iteration.
- **How to Avoid**: Always check `if cur.left` and `if cur.right` before appending to the queue.
