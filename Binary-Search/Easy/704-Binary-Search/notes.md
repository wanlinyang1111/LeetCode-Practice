# Notes for Problem number 704 - Binary Search

Link: https://leetcode.com/problems/binary-search/

## Key Concepts
- **The key concept of this problem is using Binary Search to efficiently find a target in a sorted array by repeatedly halving the search space.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Incorrect loop condition:
- **Error**: Using `while left < right` instead of `while left <= right`.
- **Reason**: This can skip checking the last remaining element, causing the algorithm to miss the target.
- **How to Avoid**: Always use `while left <= right` for an inclusive search range `[left, right]`.

### 2. Forgetting to move past mid correctly:
- **Error**: Not using `left = mid + 1` or `right = mid - 1`, e.g., writing `left = mid`.
- **Reason**: The middle element has already been checked, and failing to move past it can cause an infinite loop.
- **How to Avoid**: Always move the pointer past `mid` when updating `left` or `right`.

### 3. Not understanding `return -1`:
- **Error**: Confusion about why the function returns `-1` at the end.
- **Reason**: Returning `-1` indicates the target does not exist in the array.
- **How to Avoid**: Remember that after the loop finishes, if the target hasn’t been found, you must return `-1`.
