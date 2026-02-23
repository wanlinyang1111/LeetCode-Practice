# Notes for Problem number 704 - Binary Search

Link: https://leetcode.com/problems/binary-search/

## Key Concepts
- **The key concept of this problem is using Binary Search to efficiently find a target in a sorted array by repeatedly halving the search space.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Incorrect loop condition:
- **Error**: Using `while left < right` instead of `while left <= right`.
- **Reason**: This can skip checking the last element, causing the algorithm to miss the target.
- **How to Avoid**: Always use `while left <= right` for an inclusive search range `[left, right]`.

### 2. Forgetting to update pointers correctly:
- **Error**: Writing `left = mid` or `right = mid` instead of `left = mid + 1` or `right = mid - 1`.
- **Reason**: The middle element has already been checked, and not moving past it can lead to infinite loops.
- **How to Avoid**: Always move past `mid` when updating `left` or `right`.

### 3. Off-by-one errors:
- **Error**: Miscalculating `mid` as `(left + right + 1) // 2` unnecessarily.
- **Reason**: May shift search incorrectly depending on integer division.
- **How to Avoid**: Use `mid = (left + right) // 2` consistently unless using a specific variant of binary search.

### 4. Forgetting to handle empty array:
- **Error**: Assuming `nums` is non-empty.
- **Reason**: Accessing `nums[mid]` when `nums` is empty will throw an error.
- **How to Avoid**: Either check `if not nums: return -1` or rely on the loop condition to handle it safely.

### 5. Misunderstanding `return -1`:
- **Error**: Not returning `-1` when target is not found.
- **Reason**: Binary Search must indicate "not found"; missing this causes undefined behavior.
- **How to Avoid**: Always include `return -1` after the loop.
