class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
#Expression evaluator:
#Evaluate arithmetic expressions using a stack to store operands and operators.

def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])
    for char in expression:
        if char not in operators:
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.push(operand1 + operand2)
            elif char == '-':
                stack.push(operand1 - operand2)
            elif char == '*':
                stack.push(operand1 * operand2)
            else:
                stack.push(operand1 / operand2)
    return stack.pop()

expression = "231*+9-"
result = evaluate_postfix(expression)
print("Result:", result)
