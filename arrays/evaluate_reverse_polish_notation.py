# description: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

def evalRPN(tokens):
    stack = []
    operations = set(["+", "-", "*", "/"])

    while tokens:
        element = tokens.pop(0)
        if element not in operations:
            stack.append(int(element))
        else:
            if element == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)
            elif element == "-":
                second, first = stack.pop(), stack.pop()
                result = first - second
                stack.append(result)
            elif element == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)
            elif element == "/":
                second, first = stack.pop(), stack.pop()
                result = int(first / second) # drops the float value
                stack.append(result)

    return stack[-1]
            
        