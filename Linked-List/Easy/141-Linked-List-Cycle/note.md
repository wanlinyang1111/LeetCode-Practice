# Notes for Problem number 141 - Linked List Cycle

Link: https://leetcode.com/problems/linked-list-cycle/

## Key Concepts
- **The key concept of this problem is Floyd's Cycle Detection Algorithm (Tortoise and Hare Algorithm).**

## 🛠️ Common Errors and How to Avoid Them

### 1. Incorrect Initialization of Pointers:
- **Error**: Using `fast = slow = head` incorrectly or initializing `fast` differently.
- **Reason**: The algorithm requires both pointers to start from the same position.
- **How to Avoid**: Ensure that `fast` and `slow` are both set to `head` at the beginning.

### 2. Incorrect Loop Condition:
- **Error**: Using `while fast == slow:` instead of `while fast and fast.next:`.
- **Reason**: This causes an infinite loop since `fast` and `slow` start at the same node.
- **How to Avoid**: Use `while fast and fast.next` to ensure `fast` has valid next nodes.

### 3. Misplacing the Cycle Detection Condition:
- **Error**: Checking `if fast == slow` before moving the pointers.
- **Reason**: This leads to a false negative, as `fast` and `slow` are initially the same.
- **How to Avoid**: Move the pointers first, then check for equality.

### 4. Using `fast.val == slow.val` Instead of `fast == slow`:
- **Error**: Comparing node values instead of node references.
- **Reason**: Nodes can have duplicate values even without a cycle.
- **How to Avoid**: Always compare node references, not values.

### 5. Failing to Check for `None`:
- **Error**: Not handling cases where `head` is `None` or has only one node.
- **Reason**: Accessing `fast.next.next` when `fast` is `None` leads to an error.
- **How to Avoid**: Ensure `fast` and `fast.next` are not `None` before accessing `fast.next.next`.
