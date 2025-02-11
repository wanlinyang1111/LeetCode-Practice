# Notes for Problem number 933 - Number of Recent Calls

Link: https://leetcode.com/problems/number-of-recent-calls/description/

## Key Concepts
- **The key concept of this problem is using a deque (double-ended queue) to efficiently maintain a sliding window of time-based events.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Using a regular list instead of deque:
- **Error**: Poor performance with large inputs.
- **Reason**: Lists in Python do not have efficient `popleft()` operations; removing the first element is O(n), while `deque.popleft()` is O(1).
- **How to Avoid**: Always use `deque` when frequent front-end deletions are required.

### 2. Forgetting to remove outdated timestamps:
- **Error**: The deque keeps growing indefinitely, causing memory issues.
- **Reason**: Without the `while deque[0] < start:` loop, old timestamps are never removed.
- **How to Avoid**: Ensure that all elements outside the valid range are removed inside a loop.

### 3. Using `if` instead of `while` to remove outdated timestamps:
- **Error**: Only the first outdated timestamp is removed, but older ones remain.
- **Reason**: An `if` statement checks only once, while `while` ensures all outdated timestamps are removed.
- **How to Avoid**: Always use `while deque[0] < start:` instead of `if deque[0] < start:`.

### 4. Assigning `self.deque` to `deque` incorrectly:
- **Error**: `TypeError: 'deque' object is not callable`
- **Reason**: Overwriting the variable `deque` causes confusion between the class and the instance variable.
- **How to Avoid**: Ensure `deque = self.deque` is used properly and does not conflict with `collections.deque`.


