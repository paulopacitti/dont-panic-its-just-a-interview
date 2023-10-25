# https://leetcode.com/problems/valid-parentheses/description/
def isValid(s: str) -> bool:
    parentheses = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = []
    chars = list(s)
    for c in chars:
        if c in parentheses:
            # close chars; it has to be the last parentheses added in the stack
            if stack and stack[-1] == parentheses[c]:
                stack.pop()
            else:
                return False
        else:
            # open chars 
            stack.append(c)
    if stack:
        return False
    return True