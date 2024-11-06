# Notes for Problem number 20 - Valid Parentheses

Link: https://leetcode.com/problems/valid-parentheses/description/

## Key Concepts
- **The key concept of this problem is using a stack data structure to verify if all opening brackets have matching closing brackets in the correct order.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Missing Conditions
- **Error**: Forgetting `if not stack` to check if the stack is empty before accessing its last element.
- **Reason**: Without this check, the code will raise an error if a closing bracket appears without any prior opening brackets.
- **How to Avoid**: Always confirm that the stack is not empty before trying to access or pop from it.

### 2. Final Return Statement
- **Error**: Returning `True` prematurely without verifying that the stack is empty at the end.
- **Reason**: The stack must be completely empty by the end of the iteration for the string to be considered valid.
- **How to Avoid**: Ensure `return not stack` is used as the last line so it confirms no unmatched opening brackets remain.

### 3. Clear if-else Logic
- **Error**: Mixing up conditions for different brackets, causing incorrect matches.
- **Reason**: Each closing bracket must be paired with its corresponding opening bracket.
- **How to Avoid**: Use `elif` statements to clearly handle each bracket type individually, and avoid any overlap in matching conditions.

### 4. Confusing Queue with Stack
- **Error**: Mistaking stack operations for queue operations (e.g., using a queue approach instead of `pop` for stack).
- **Reason**: The stack requires a last-in, first-out (LIFO) approach, which depends on `pop` to remove the last element.
- **How to Avoid**: Remember that stacks use `pop()` to match and remove elements in LIFO order.

### 5. Using `string` Instead of `char`
- **Error**: Using `string` as the variable name when iterating over individual characters.
- **Reason**: The variable represents each character in the string `s`, so `char` is a more accurate and descriptive name.
- **How to Avoid**: Use `char` as the variable name to clearly indicate it refers to single characters rather than the entire string.
