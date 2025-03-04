# You are given an array of string `tokens` representing an arithmetic 
# expression in Reverse Polish Notation (RPN). 
# Your task is to evaluate the expression and return an integer result.

# In RPN, each token is either:
# 1. An **operand** (integer).
# 2. An **operator** (`+`, `-`, `*`, `/`).

# The evaluation follows a **stack-based approach** (LIFO - Last In, First Out).

# ---- UMPIRE Method ----

# 1️⃣ **Understand**:
# - The input is guaranteed to be a **valid RPN expression**.
# - Division truncates **towards zero**.
# - The result fits within a **32-bit integer**.
# - There is **no division by zero**.

# 2️⃣ **Match**:
# - This is a **stack-based** problem.
# - We must process the tokens **sequentially**.

# 3️⃣ **Plan**:
# - Initialize an **empty stack**.
# - Iterate through `tokens`:
#   - If `token` is a **number**, convert it to `int` and push it onto the stack.
#   - If `token` is an **operator**, pop the top two elements, perform the operation, and push the result back.
# - At the end, return the last remaining number in the stack.

# 4️⃣ **Implement**:
# ✅ Correct Code:
# def evalRPN(self, tokens: List[str]) -> int:
#     stack = []
#     for token in tokens:
#         if token not in {"+", "-", "*", "/"}:
#             stack.append(int(token))
#         else:
#             b = stack.pop()  # Last inserted number
#             a = stack.pop()  # Second-last inserted number
#             if token == "+":
#                 stack.append(a + b)
#             elif token == "-":
#                 stack.append(a - b)
#             elif token == "*":
#                 stack.append(a * b)
#             else:  # Division (truncated towards zero)
#                 stack.append(int(a / b))
#     return stack[-1]  # Final result

# 5️⃣ **Review**:
# - ✅ Uses a **stack-based** approach.
# - ✅ Ensures correct **order of operations**.
# - ✅ Handles **integer division correctly**.

# 6️⃣ **Evaluate**:
# - Time Complexity: **O(n)**
# - Space Complexity: **O(n)** (for the stack)
