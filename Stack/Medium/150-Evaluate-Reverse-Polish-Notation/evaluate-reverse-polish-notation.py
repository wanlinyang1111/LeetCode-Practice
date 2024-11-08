class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []                                                                 # Initialize an empty stack to store intermediate results

        for token in tokens:                                                       # Iterate through each token in the input
            if token != "+" and token != "-" and token != "*" and token != "/":    # If the token is a number
                stack.append(int(token))                                           # Convert the token to an integer and push it onto the stack
            else:                                                                  # If the token is an operator
                b = stack.pop()                                                    # Pop the last number from the stack as the second operand
                a = stack.pop()                                                    # Pop the next number from the stack as the first operand
                if token == "+":                                                   # If the operator is '+'
                    stack.append(a + b)                                            # Push the result of a + b back onto the stack
                elif token == "-":                                                 # If the operator is '-'
                    stack.append(a - b)                                            # Push the result of a - b back onto the stack
                elif token == "*":                                                 # If the operator is '*'
                    stack.append(a * b)                                            # Push the result of a * b back onto the stack
                else:                                                              # If the operator is '/' (division)
                    stack.append(int(a / b))                                       # Perform integer division and push the result onto the stack
        return stack[0]                                                            # Return the last remaining item in the stack, which is the final result
