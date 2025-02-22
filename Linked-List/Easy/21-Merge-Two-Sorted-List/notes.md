# Notes for Problem number xxx - Merge Two Sorted Lists

Link: https://leetcode.com/problems/merge-two-sorted-lists/

## Key Concepts
- **The key concept of this problem is merging two sorted linked lists efficiently using iteration.**
- **We use a dummy node to simplify pointer operations and avoid extra condition checks.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Forgetting to move `l1` or `l2` forward:
- **Error**: Not updating `l1` or `l2` after attaching a node.
- **Reason**: This causes an infinite loop or repeated attachments of the same node.
- **How to Avoid**: Always advance `l1 = l1.next` or `l2 = l2.next` after attaching a node.

### 2. Incorrectly linking the smaller node:
- **Error**: Using `if l1.val >= l2.val`, which attaches the larger value instead.
- **Reason**: The correct order is non-decreasing, so `l1` should be attached when `l1.val <= l2.val`.
- **How to Avoid**: Use `if l1.val <= l2.val` to ensure a proper merge order.

### 3. Missing the final attachment step:
- **Error**: Not handling the case where one list is fully merged before the other.
- **Reason**: This causes missing nodes in the final linked list.
- **How to Avoid**: After exiting the loop, attach the remaining part of `l1` or `l2`.

### 4. Not initializing a dummy node:
- **Error**: Trying to merge directly without a dummy node.
- **Reason**: This makes pointer handling more complex and requires extra edge case checks.
- **How to Avoid**: Use a dummy node (`dum = ListNode(-1)`) to simplify pointer updates.
