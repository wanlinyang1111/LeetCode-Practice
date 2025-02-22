# Notes for Problem number 206 - Reverse Linked List

Link: https://leetcode.com/problems/reverse-linked-list/

## Key Concepts
- **The key concept of this problem is pointer manipulation in a linked list.**  
- **We need to reverse the direction of the pointers while traversing the list iteratively.**  

## 🛠️ Common Errors and How to Avoid Them  

### 1. Incorrectly updating `prev`:
- **Error**: Setting `prev = curr` before updating `curr.next`, leading to incorrect pointer references.  
- **Reason**: If `curr.next` is not updated before moving `prev`, the next node will still point to the original order.  
- **How to Avoid**: Always update `curr.next = prev` before moving `prev` forward.  

### 2. Not handling edge cases (empty list or single-node list):  
- **Error**: The function does not return correctly when `head` is `None` or has only one node.  
- **Reason**: If `head` is `None`, the loop will never run, and `prev` should remain `None`.  
- **How to Avoid**: Ensure the function works properly even if `head` is `None` or has just one node.  

### 3. Using an incorrect loop condition:  
- **Error**: Using `while curr and curr.next`, which skips processing the last node.  
- **Reason**: The last node’s pointer is not updated, leading to an incomplete reversal.  
- **How to Avoid**: Use `while curr` to process all nodes, including the last one.  

### 4. Misunderstanding the role of `temp`:  
- **Error**: Forgetting to store `curr.next` in `temp`, leading to lost references to the remaining list.  
- **Reason**: If `curr.next` is not saved before updating `curr.next = prev`, the rest of the list becomes unreachable.  
- **How to Avoid**: Always store `curr.next` in `temp` before modifying `curr.next`.  

### 5. Returning `curr` instead of `prev` at the end:  
- **Error**: The function returns `curr` instead of `prev`, which does not point to the new head.  
- **Reason**: `curr` becomes `None` when the loop exits, so returning it results in `None` instead of the reversed list.  
- **How to Avoid**: Return `prev`, which correctly holds the new head after all nodes have been reversed.  
