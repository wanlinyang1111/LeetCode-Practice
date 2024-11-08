# Notes for Problem number 150 - Evaluate Reverse Polish Notation

Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

## Key Concepts
- **The key concept of this problem is stack-based evaluation of expressions**  
   Reverse Polish Notation (RPN) requires evaluating expressions in a specific order, using a stack to manage operands and apply operators.

## 🛠️ Common Errors and How to Avoid Them

### 1. Using `and` instead of `or` in the first line for operator check:
- **Error**: Using `or` in the `if` condition to check if a token is not an operator.
- **Reason**: Using `or` would incorrectly allow non-operators to bypass the intended check, leading to operators being mistakenly pushed to the stack as numbers.
- **How to Avoid**: Always use `and` to ensure all conditions are checked as required. For example:
    ```python
    if token != "+" and token != "-" and token != "*" and token != "/":
    ```

### 2. Missing `()` after `pop` when using `stack.pop`:
- **Error**: Writing `stack.pop` without `()` leads to using the function itself, not the returned value.
- **Reason**: Without `()`, Python treats `stack.pop` as a function reference, not an actual method call.
- **How to Avoid**: Always add `()` to call the method correctly, like this:
    ```python
    b = stack.pop()
    ```

### 3. Carefully reviewing problem rules to apply correct logic:
- **Error**: Misinterpreting rules or confusing logic with similar problems.
- **Reason**: Skimming problem statements or using assumptions based on past problems can cause mistakes in logic.
- **How to Avoid**: Pay attention to specific problem requirements. Approach each problem independently to prevent misinterpretation.
