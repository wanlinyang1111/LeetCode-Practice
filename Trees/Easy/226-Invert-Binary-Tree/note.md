# Notes for Problem number 226 - Invert Binary Tree

Link: https://leetcode.com/problems/invert-binary-tree/

## Key Concepts
- **The key concept of this problem is recursive DFS (Depth-First Search)**  
- We recursively traverse each node and swap its left and right children.

## 🛠️ Common Errors and How to Avoid Them

### 1. Using BFS unnecessarily:
- **Error**: Tried to implement the solution using BFS (queue-based level traversal), but got confused.
- **Reason**: BFS is not wrong, but recursive DFS is much more intuitive and easier to implement for this problem.
- **How to Avoid**: Start with DFS unless there's a clear reason to use BFS. It aligns better with the structure of tree problems.

### 2. Forgetting to use `self.`:
- **Error**: Called `invertTree()` recursively without `self.`.
- **Reason**: Inside a class, methods must be accessed with `self.` unless they are static or external functions.
- **How to Avoid**: Always use `self.` when calling methods from within a class.

### 3. Confusion between self-defined helper and LeetCode default method:
- **Error**: Not sure when to define my own `def invert()` versus using the class method directly.
- **Reason**: If you define your own function inside a method, don’t use `self.`. But if you're using the given LeetCode method, you must use `self.`.
- **How to Avoid**: Understand the execution context—LeetCode calls the method via a `Solution` instance, so `self.` is needed.

### 4. Recursive logic is hard to visualize:
- **Error**: Hard to mentally simulate the recursive calls and swaps.
- **Reason**: Tree recursion can be abstract and difficult without visual support.
- **How to Avoid**: Always draw the tree or use visualization tools to track recursive operations.

### 5. Overcomplicating the base case:
- **Error**: Tried to handle too many edge cases.
- **Reason**: The only base case needed is `if not root: return None`.
- **How to Avoid**: Keep recursion clean. For binary tree traversal, usually only one base case is enough.
- 
