# Notes for Problem number 876 - Middle of the Linked List

Link: https://leetcode.com/problems/middle-of-the-linked-list/

## Key Concepts
- **The key concept of this problem is the Two-Pointer (Fast & Slow) technique.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Incorrect `while` loop condition:
- **Error**: Using `while fast.next and fast:`
- **Reason**: `fast.next` is checked before `fast`, which may cause an AttributeError if `fast` is `None`.
- **How to Avoid**: Use `while fast and fast.next:` to ensure `fast` is not `None` before accessing `fast.next`.

### 2. Moving `fast` pointer incorrectly:
- **Error**: Updating `fast = fast.next` instead of `fast = fast.next.next`
- **Reason**: This causes `fast` to move only one step instead of two, making it behave like the slow pointer.
- **How to Avoid**: Ensure `fast = fast.next.next` to maintain the two-step movement.

### 3. Forgetting to initialize both pointers:
- **Error**: Not setting `slow = fast = head` at the beginning.
- **Reason**: If `slow` and `fast` are not initialized to `head`, the loop will not function properly.
- **How to Avoid**: Always initialize both pointers at `head`.

### 4. Not handling edge cases:
- **Error**: Not considering cases where the linked list has only one node.
- **Reason**: If `head` contains only one node, `fast.next` does not exist.
- **How to Avoid**: The condition `while fast and fast.next:` naturally prevents errors in this case.

### 5. Returning `fast` instead of `slow`:
- **Error**: Mistakenly returning `fast` at the end.
- **Reason**: The problem requires returning the middle node, which is tracked by `slow`.
- **How to Avoid**: Always return `slow`, as it correctly points to the middle node.
