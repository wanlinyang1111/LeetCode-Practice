# Notes for Problem number 104 - Maximum Depth of Binary Tree

Link: [https://leetcode.com/problems/maximum-depth-of-binary-tree/](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

## Key Concepts
- **The key concept of this problem is using BFS (Breadth-First Search) to traverse the tree level by level and count how many levels (depth) the tree has.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Incorrect variable naming for the queue
- **Error**: Using variable names like `res` instead of something meaningful like `queue` or `q`.
- **Reason**: This can lead to confusion, especially when the queue is used for traversal, not for storing results.
- **How to Avoid**: Use descriptive names like `queue` or `mark` when implementing BFS.

### 2. Missing base case: `if not root: return 0`
- **Error**: Forgot to check if the tree is empty.
- **Reason**: If root is `None`, the while loop will never run, and it may lead to incorrect behavior or errors.
- **How to Avoid**: Always add a base case check before starting BFS or DFS.

### 3. Placing BFS logic inside an unnecessary nested function
- **Error**: Defining a separate `bfs()` function inside `maxDepth` when not needed.
- **Reason**: Adds unnecessary complexity and may introduce scope-related bugs.
- **How to Avoid**: Write the BFS loop directly inside the main function when the logic is short and straightforward.

### 4. Forgetting to return the correct variable
- **Error**: Forgot to return `count` at the end.
- **Reason**: Without returning the depth counter, the function may return `None` by default.
- **How to Avoid**: Always confirm you return the final computed value.

### 5. Misplacing the `pop(0)` outside the for loop
- **Error**: Writing `cur = queue.pop(0)` **before** the for loop.
- **Reason**: Only one node gets popped and processed, while the loop reuses the same node.
- **How to Avoid**: Pop each node **inside** the for loop to ensure every node in the current level is processed properly.

---

## ✅ Takeaway
Remember this BFS pattern:
> 🧠 “Use `while` to count levels, use `for` to process nodes.”
