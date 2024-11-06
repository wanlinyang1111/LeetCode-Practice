class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []                                         # Initialize an empty stack to keep track of opening brackets

        for char in s:                                     # Iterate through each character in the string `s`
            if char == "(" or char == "{" or char == "[":  # Check if the character is an opening bracket
                stack.append(char)                         # If so, add it to the stack
            else:
                if not stack:                              # If the stack is empty, there’s no opening bracket to match, so return False
                    return False
                if char == ")" and stack[-1] == "(":       # If the character is a closing parenthesis and matches the last opening one
                    stack.pop()                            # Remove the matched opening bracket from the stack
                elif char == "]" and stack[-1] == "[":     # If the character is a closing bracket for square brackets
                    stack.pop()                            # Remove the matched opening square bracket
                elif char == "}" and stack[-1] == "{":     # If the character is a closing bracket for curly brackets
                    stack.pop()                            # Remove the matched opening curly bracket
                else:
                    return False                           # If the closing bracket does not match, return False
        return not stack                                   # Return True if the stack is empty (all brackets were matched), otherwise False
