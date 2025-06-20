# Notes for Problem number 125 - Valid Palindrome

Link: https://leetcode.com/problems/valid-palindrome/

## Key Concepts
- **The key concept of this problem is using two pointers to compare characters from both ends after preprocessing the string to remove non-alphanumeric characters.**

## 🛠️ Common Errors and How to Avoid Them

### 1. Using `char.isalnum` instead of `char.isalnum()`:
- **Error**: Typo in method name or missing parentheses.
- **Reason**: `isalnum` is a method, not a variable. Forgetting the `()` will store a function reference, not a boolean value.
- **How to Avoid**: Always double-check method names and ensure you use parentheses when calling string methods.

### 2. Writing `char.lower` instead of `char.lower()`:
- **Error**: Lowercase conversion doesn’t happen.
- **Reason**: Similar to above, `lower` is a method that needs to be called.
- **How to Avoid**: Add `()` to properly convert the character to lowercase.

### 3. Comparing characters using fixed indices like `test[0] == test[-1]` in a loop:
- **Error**: Only compares the first and last characters, doesn't iterate.
- **Reason**: Logic does not account for the rest of the string.
- **How to Avoid**: Use a while loop with two pointers (`left`, `right`) and increment/decrement them in each iteration to compare all relevant characters.

### 4. Incorrect `while` condition
- **Error**:  The loop does not properly check whether the two pointers (`left` and `right`) have crossed. This can lead to infinite loops or `IndexError` when accessing out-of-bound indices
- **Reason**:  Without explicit control over when to stop, the logic fails when the two pointers meet or cross.
- **How to Avoid**:  Use `while left < right:` to clearly define the loop boundary. This ensures that comparisons only occur while the left pointer is to the left of the right pointer, and avoids unnecessary or invalid comparisons.

