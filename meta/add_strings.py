# description: https://leetcode.com/problems/add-strings/submissions/
# tags: greedy

def add_strings(num1, num2):
    sum = ""
    carry = 0

    if len(num1) < len(num2):
        num1, num2 = num2, num1

    i = len(num1) - 1
    j = len(num2) - 1

    while i >= 0 or j >= 0:
        if j >= 0:   
            current = (ord(num1[i]) - ord("0")) + (ord(num2[j]) - ord("0")) + carry
        else:
            current = (ord(num1[i]) - ord("0")) + carry

        if current >= 10:
            current -= 10
            carry = 1
        else:
            carry = 0

        i -= 1
        j -= 1
        sum += str(current)
    
    if carry == 1:
        sum += str(carry)
    return sum[::-1]

a = "11"
b = "123"
print(add_strings(a, b))
    
# Time complexity: O(m + n), where m is the lenght of the first parameter, and n the second one
# Space complexity: O(m + n)