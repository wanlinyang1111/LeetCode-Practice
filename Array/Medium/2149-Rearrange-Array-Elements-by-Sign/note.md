# Notes for Problem 2149 - Rearrange Array Elements by Sign

Link: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

## Key Concepts
- **The key concept of this problem is to rearrange an array of integers such that every consecutive pair consists of one positive and one negative number, while maintaining the original order of elements within their respective signs, starting with a positive integer.**

## 🛠️ Common Mistakes and How to Avoid Them 

1. **Using `for i in range` vs. `for i in range(len(...))`**:
   - **Error**: Using `for i in range:` without specifying `len(...)` can lead to unexpected results or an incomplete iteration.
   - **Reason**: The concept of iterating over a range needs to be clearly understood, especially how to use `len()` to iterate through the length of an array.
   - **How to Avoid**: Always use `range(len(array))` when iterating over indices of an array to ensure you cover all elements.

2. **Using Square Brackets `[]` for Lists vs. Parentheses `()`**:
   - **Error**: Confusing the syntax for lists with tuples or other data types by using `()`.
   - **Reason**: This confusion arises from not clearly understanding the differences between data structures in Python.
   - **How to Avoid**: Remember that lists are defined using square brackets `[]`. Make a habit of checking the syntax when declaring lists.

3. **Spelling Mistakes in Keywords like `return`**:
   - **Error**: Misspelling the keyword `return` can cause the code to fail without syntax highlighting in some IDEs.
   - **Reason**: Being unaware that certain keywords are case-sensitive and must be spelled correctly.
   - **How to Avoid**: Double-check keywords and their spelling. Use an IDE that provides syntax highlighting and error detection to catch these mistakes early.

By reflecting on these common pitfalls, you can enhance your understanding and avoid making similar mistakes in future coding challenges. Happy coding! 😊
