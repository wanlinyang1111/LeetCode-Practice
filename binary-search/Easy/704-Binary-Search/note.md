# Notes for Problem number 704 - Binary Search

Link: https://leetcode.com/problems/binary-search/

## Key Concepts
- **The key concept of this problem is binary search on a sorted array, using the divide and conquer approach to reduce the search space by half each step (O(log n) time complexity).**

## 🛠️ Common Errors and How to Avoid Them

### 1. Not realizing this is a binary search problem:
- **Error**: Solved the problem using a linear search (O(n) time complexity).
- **Reason**: Missed the key detail that the input array is sorted.
- **How to Avoid**: When a problem involves searching in a sorted array, always consider using binary search first.

### 2. Returning too early inside a loop:
- **Error**: Returning `-1` immediately after the first mismatch in a for-loop.
- **Reason**: This causes the loop to terminate after checking only the first element.
- **How to Avoid**: Place `return -1` **after** the loop ends, not inside the `else`.

### 3. Incorrect list length calculation:
- **Error**: Using `len(nums-1)` instead of `len(nums) - 1`.
- **Reason**: `nums - 1` is an invalid operation, and `len()` must be called on a list.
- **How to Avoid**: Always apply `len()` to the list first, then subtract.

### 4. Wrong while-loop condition:
- **Error**: Using `while left < right` instead of `while left <= right`.
- **Reason**: This skips checking the case when `left == right`, which could be the answer.
- **How to Avoid**: Use `<=` to ensure all possible positions are checked.
