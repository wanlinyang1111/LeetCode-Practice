# Notes for Problem number 1 - Two Sum

Link: https://leetcode.com/problems/two-sum/description/

## Key Concepts
- **The key concept of this problem is using a hash table (dictionary) to store numbers and their indices**. This allows for fast look-up of the needed complement to reach the target sum

## 🛠️ Common Errors and How to Avoid Them

### 1. Using `enumerate` for index and value:
- **Error**: Forgetting to use `enumerate` in the `for` loop.
- **Reason**: We need both the index and the value in each iteration to store and retrieve values for the final answer.
- **How to Avoid**: Use `for index, num in enumerate(nums)` to access both the number and its index.

### 2. Order of `enumerate` arguments:
- **Error**: Reversing `index` and `num` in `enumerate` (e.g., `for num, index in enumerate(nums)`).
- **Reason**: `enumerate(nums)` returns `(index, value)`, not `(value, index)`.
- **How to Avoid**: Use the format `for index, num in enumerate(nums)` to prevent mismatched values.

### 3. Coding Style: Naming and Spacing:
- **Error**: Using unclear names like `hash` or inconsistent spacing.
- **Reason**: Using descriptive names and consistent spacing improves readability and avoids using built-in Python functions (e.g., `hash`).
- **How to Avoid**: Name variables clearly, like `num_to_index`, and add spaces around operators for readability (e.g., `remain = target - num`).
