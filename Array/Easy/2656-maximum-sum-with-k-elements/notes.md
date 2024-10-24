# Notes for Problem 2656 - Maximum Sum With Exactly K Elements

Link: https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/

## Key Concepts
- **The key concept of this problem is to select exactly k elements from an array such that their sum is maximized.**

## Common Mistakes and How to Avoid Them

### 1. Incorrect Variable Usage
- **Mistake**: Using `tem += score` instead of `score += tem`.
- **Reason**: This can lead to incorrect calculations of the total score.
- **How to Avoid**: Always double-check variable names and ensure you're updating the correct variable in your calculations.

### 2. Indentation Issues
- **Mistake**: Not maintaining consistent indentation within the function definition.
- **Reason**: This can cause syntax errors or logical errors in code execution.
- **How to Avoid**: Use an IDE or text editor that highlights indentation levels and ensure all code inside the function is properly indented.

### 3. Missing Range in For Loop
- **Mistake**: Forgetting to use `for i in range(k)` in the loop.
- **Reason**: This will prevent the loop from executing the intended number of times to select `k` elements.
- **How to Avoid**: Always verify loop constructs and ensure they cover the desired range.
