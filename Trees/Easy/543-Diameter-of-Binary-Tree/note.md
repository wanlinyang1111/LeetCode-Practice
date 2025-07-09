# Notes for Problem number 543 - Diameter of Binary Tree

Link: https://leetcode.com/problems/diameter-of-binary-tree/

## Key Concepts
- **The key concept of this problem is to use post-order DFS to calculate the height of each subtree and update the diameter by comparing left and right subtree heights at each node.**
- A global variable (`self.res`) is used to track the maximum diameter across all recursive calls.

## 🛠️ Common Errors and How to Avoid Them

### 1. Forgetting the base case in DFS:
- **Error**: `return 0` is missing when `root is None`.
- **Reason**: Without the base case, recursion goes infinitely and crashes with a `RecursionError`.
- **How to Avoid**: Always start DFS functions by checking `if not root: return 0`.

### 2. Mixing up `res` and `self.res`:
- **Error**: Using both `res = 0` and `self.res = ...` inconsistently.
- **Reason**: `res` is a local variable and cannot be updated inside a nested function; `self.res` is needed to persist updates across all DFS calls.
- **How to Avoid**: Use `self.res` consistently to share state across recursion.

### 3. Confusion about what to return in DFS:
- **Error**: Unclear whether to return a list, height, or boolean.
- **Reason**: The goal is to return the **height** of the current subtree to the parent call.
- **How to Avoid**: Remember this pattern: "DFS returns height; diameter is updated via side effect."

### 4. Forgetting post-order traversal structure:
- **Error**: Trying to calculate diameter before getting left and right subtree heights.
- **Reason**: You need both subtree heights to compute `left + right`.
- **How to Avoid**: Always structure the DFS as post-order: left → right → process node.

### 5. Variable naming confusion (e.g., is it a number or a list?):
- **Error**: Misnaming variables (e.g., `left = dfs(...)` but think it’s a list or a node).
- **Reason**: Recursive DFS returns **integer height**, not nodes or lists.
- **How to Avoid**: Clarify in your mind and comments: `dfs()` returns an `int`, not a node or list.

