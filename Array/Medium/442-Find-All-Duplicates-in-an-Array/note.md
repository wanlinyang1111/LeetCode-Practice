# Notes for Problem number 442 - Find All Duplicates in an Array

Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/

## Key Concepts
- **The key concept of this problem is to identify duplicates in an array within a range by marking visited indices, meeting the O(n) time complexity and O(1) auxiliary space requirements.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Not Meeting Constant Space Requirement:
- **Error**: Using data structures like `set` or `dict` for tracking duplicates.
- **Reason**: This problem requires constant auxiliary space, meaning additional data structures that grow with input size are not allowed, except for the return array.
- **How to Avoid**: Mark visited indices within the array itself, as the numbers fall within a range that allows in-place modifications.

### 2. Misinterpreting the Number Range:
- **Error**: Incorrectly managing indices without considering the 1-based to 0-based index mapping.
- **Reason**: The problem specifies that numbers are within the range `[1, n]`, which requires careful adjustment to use array indices for marking.
- **How to Avoid**: Always use `abs(num) - 1` when marking to handle the range correctly and avoid out-of-bounds errors.

### 3. Inconsistent Variable Naming:
- **Error**: Using unclear or inconsistent names for variables like `index` or `ans_arr`.
- **Reason**: Ambiguous naming can cause confusion during coding and debugging.
- **How to Avoid**: Use clear, descriptive names that make the purpose of each variable obvious, like `duplicate_list` or `visited_index`.

### 4. Incorrect Use of Append:
- **Error**: Attempting to append using `append()` on non-list types, such as dictionaries or sets.
- **Reason**: `append()` is specific to lists in Python, and using it on other types causes runtime errors.
- **How to Avoid**: Only use `append()` with lists. For sets, use `add()` instead.

### 5. Misuse of `dict` and `set` for Printing:
- **Error**: Using `dict.items()` or `set.add()` incorrectly.
- **Reason**: If you use a dictionary for counting (though it doesn’t meet the space requirement), you must use `dict.items()` for key-value pairs when printing.
- **How to Avoid**: For sets, use `set.add()` for adding elements; avoid using `.append()` as it's not valid for sets. For dictionaries, use `.items()` to access both keys and values when printing.

