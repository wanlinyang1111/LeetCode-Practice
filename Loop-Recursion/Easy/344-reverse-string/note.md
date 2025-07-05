# Notes for Problem 344 - Reverse String

Link: https://leetcode.com/problems/reverse-string/

## Key Concepts
- **The key concept of this problem is in-place string reversal using recursion**.
- **Recursion works by breaking down the problem into smaller subproblems until a base case is reached**.
- **In-place modification means swapping elements within the given array without using extra memory**.

## 🛠️ Common Errors and How to Avoid Them

### 1. Forgetting the base case:
- **Error**: The recursive function runs indefinitely, causing a stack overflow.
- **Reason**: Without a stopping condition, recursion continues infinitely.
- **How to Avoid**: Always include a base case (`if l >= r: return`) to terminate recursion.

### 2. Incorrectly swapping elements:
- **Error**: The elements are not swapped correctly, leading to an incorrect result.
- **Reason**: Forgetting to swap `s[l]` and `s[r]` before making the recursive call.
- **How to Avoid**: Ensure that `s[l], s[r] = s[r], s[l]` executes before calling the next recursion step.

### 3. Misunderstanding how indices (`l` and `r`) work:
- **Error**: Thinking `l` and `r` automatically map to `s[0]` and `s[len(s) - 1]` without explicitly passing them.
- **Reason**: `l` and `r` are just integer values representing positions, not directly tied to the array unless passed explicitly.
- **How to Avoid**: Understand that `reverse(0, len(s)-1, s)` explicitly defines their starting positions.

### 4. Thinking recursion is the only solution:
- **Error**: Assuming recursion is necessary when an iterative approach may be simpler.
- **Reason**: A loop with two pointers swapping elements is more intuitive and uses `O(1)` space.
- **How to Avoid**: Consider using an iterative approach when space complexity is a concern.

