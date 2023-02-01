#Parenthesis matching:
#Check if a given expression has matching parentheses using a stack. code

def check_parenthesis(expr):
    stack = []
    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        elif char in [")", "}", "]"]:
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            stack.pop()
    return not stack

print(check_parenthesis("()")) # True
print(check_parenthesis("{[()]}")) # True
print(check_parenthesis("{[(])}")) # False