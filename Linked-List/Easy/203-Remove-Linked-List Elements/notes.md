# Notes for Problem number 203 - Remove Linked List Elements

Link: https://leetcode.com/problems/remove-linked-list-elements/

## Key Concepts
- **The key concept of this problem is linked list traversal using two pointers (prev and curr) to modify the list in-place.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Not handling the case where the head node itself needs to be removed:
- **Error**: The solution does not check if the head node contains the target value before entering the loop.
- **Reason**: If the head node is not properly checked, the function may return an incorrect list or cause an error when accessing `prev.next`.
- **How to Avoid**: Use a `while` loop at the beginning to move `head` forward until it points to a node that does not need to be removed.

### 2. Forgetting to update `prev` when removing a node:
- **Error**: If `curr` is removed but `prev` is not updated correctly, the link between nodes may be broken.
- **Reason**: When deleting a node, failing to update `prev` can lead to an incorrect pointer structure in the linked list.
- **How to Avoid**: Ensure that `prev` is only updated when `curr` is not removed.

### 3. Incorrectly updating `curr` after deletion:
- **Error**: `curr` is not advanced properly, leading to skipped nodes or infinite loops.
- **Reason**: If `curr` is reassigned incorrectly within the loop, the iteration logic may fail.
- **How to Avoid**: Always update `curr = curr.next` at the end of each loop iteration to ensure proper traversal.
