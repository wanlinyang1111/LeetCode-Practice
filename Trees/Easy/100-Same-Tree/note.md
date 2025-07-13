# Notes for Problem number 100 - Same Tree

Link: https://leetcode.com/problems/same-tree/

## Key Concepts
- **The key concept of this problem is recursive tree comparison**
- We traverse both trees simultaneously, and check:
  - If both nodes are None → same
  - If one node is None or values differ → not the same
  - Otherwise, continue checking left and right subtrees recursively

## 🛠️ Common Errors and How to Avoid Them

### 1. Not handling the base case correctly:
- **Error**: Forgetting to check if both `p` and `q` are `None`.
- **Reason**: This leads to AttributeError when trying to access `.val` or `.left` of a NoneType.
- **How to Avoid**: Always write `if not p and not q: return True` as your first check.

---

### 2. Using `isSameTree(...)` instead of `self.isSameTree(...)`:
- **Error**: Calling the function without `self.` inside the class method.
- **Reason**: In Python, methods defined in a class must be accessed via `self` unless declared as `@staticmethod`.
- **How to Avoid**: Remember to use `self.` when calling recursive methods inside the same class.

---

### 3. Writing conditions in the wrong order:
- **Error**: Checking `p.val == q.val` before confirming `p` and `q` are not `None`.
- **Reason**: Will throw an error if either node is `None`.
- **How to Avoid**: Always check nullity (`None`) before comparing values.

---

### 4. Thinking the recursive call changes the node structure:
- **Error**: Expecting recursion to update the original tree nodes.
- **Reason**: This function is only for comparison, not mutation.
- **How to Avoid**: Understand that recursion here only **checks** equality, it does not modify.

---

### 5. Confusing this with tree traversal problems:
- **Error**: Trying to use inorder/preorder/postorder traversal unnecessarily.
- **Reason**: This is not a traversal output matching problem, but a node-by-node structural comparison.
- **How to Avoid**: Focus on base case + recursive left and right checks. Keep it simple.

