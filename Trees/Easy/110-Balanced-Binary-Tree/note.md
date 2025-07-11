# Notes for Problem number 110 - Balanced Binary Tree

Link: https://leetcode.com/problems/balanced-binary-tree/

## Key Concepts
- **The key concept of this problem is post-order DFS traversal to compute both balance status and height from bottom up.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Forgetting to return the result in the main function
- **Error**: `dfs(root)[0]` was written, but not returned.
- **Reason**: Calling the function computes the result, but if it's not returned, the main function returns `None`.
- **How to Avoid**: Always remember to write `return dfs(root)[0]` in the last line of the main function.

### 2. Not returning the height from the `dfs` helper
- **Error**: Only returned whether the subtree was balanced, but forgot the height.
- **Reason**: Height is required to compute the balance condition in parent nodes.
- **How to Avoid**: Always return both `[isBalanced, height]` from `dfs`.

### 3. Confusing the structure of the return value
- **Error**: Tried to write `return isbal, height` and accessed them with indexing like a list.
- **Reason**: Mixing up tuple vs list syntax caused inconsistency.
- **How to Avoid**: Be consistent—use either list (`[True, 2]`) or tuple (`(True, 2)`) and access accordingly.

### 4. Misunderstanding the base case
- **Error**: Didn't know what to return when `root` is `None`.
- **Reason**: Unsure if an empty subtree should be considered balanced.
- **How to Avoid**: Remember that an empty tree is considered balanced with height 0: `return [True, 0]`.

### 5. Putting the balance check in the wrong place
- **Error**: Tried to check balance before finishing both left and right subtree traversal.
- **Reason**: Didn't follow post-order logic.
- **How to Avoid**: Always check balance after computing both left and right subtrees.
