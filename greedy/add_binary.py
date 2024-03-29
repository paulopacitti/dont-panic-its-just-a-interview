# description: https://leetcode.com/problems/add-binary
# 0 + 0 = 0
# 1 + 0 = 1
# 1 + 1 = 0 + carry
# 1 + 1 + 1 = 1 + carry


def addBinary(a, b):
    result = ""
    carry = 0
    a = a[::-1]
    b = b[::-1]

    for i in range((max(len(a), len(b)))):
        a_bit = ord(a[i]) - ord("0") if i < len(a) else 0
        b_bit = ord(b[i]) - ord("0") if i < len(b) else 0

        current = a_bit + b_bit + carry
        result += str(current % 2)
        carry = current // 2
    if carry:
        result += "1"
    return result[::-1]



a = "11"
b = "1"
print(addBinary(a, b))
