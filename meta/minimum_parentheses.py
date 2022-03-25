# description: https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
def minimum_parentheses(s):
    stack_open = [] # only opening parentheses
    word = list(s)

    for index, char in enumerate(word):
        if char == '(':
            stack_open.append(index)
        elif char == ')':
            if stack_open: # check if opening parentheses happened early
                stack_open.pop() # close parentheses
            else:
                word[index] = '' # remove char, because do not closed parentheses
        
    for i in stack_open:  # removes every opened parentheses not closed
        word[i] = ''
    return ''.join(word)

print(minimum_parentheses('lee(t(c)o)de)'))

# Time complexity: O(l), where l is the lenght of the string
# Space complexity: O(l)