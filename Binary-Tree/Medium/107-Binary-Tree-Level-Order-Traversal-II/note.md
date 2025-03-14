# Notes for Problem 107 - Binary Tree Level Order Traversal II

Link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

## Key Concepts
- **The key concept of this problem is level-order traversal using a queue (BFS)**.
- Instead of returning the values from top to bottom, we reverse the order to return them from bottom to top.

## 🛠️ Common Errors and How to Avoid Them

### 1. Forgetting the base case (`if not root: return []`)
- **Error**: Missing the condition to handle an empty tree.
- **Reason**: If `root` is `None`, the function should return an empty list.
- **How to Avoid**: Always check for edge cases at the beginning of the function.

### 2. Incorrectly reversing the result
- **Error**: Using `reversed(ans)` without converting it to a list.
- **Reason**: `reversed()` returns an iterator, not a list.
- **How to Avoid**: Use `list(reversed(ans))` to ensure the output format is correct.

### 3. Syntax error: Typo in `not`
- **Error**: Writing `no` instead of `not` when checking `if not root:`.
- **Reason**: `no` is not a valid Python keyword, but the lack of syntax highlighting made the mistake hard to notice.
- **How to Avoid**: Be mindful of typos, and use an editor with syntax highlighting.

### 4. Not appending levels to `ans` correctly
- **Error**: Forgetting `if temp:` before appending the level to `ans`.
- **Reason**: If `temp` is empty, appending it can cause unintended results.
- **How to Avoid**: Always check if `temp` contains values before appending it to `ans`.
