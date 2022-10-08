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

    for i in range(max(len(a), len(b))):
        digit_a = ord(a[i]) - ord(0) if i < len(a) else 0
        digit_b = ord(b[i]) - ord(0) if i < len(b) else 0

        current = digit_a + digit_b + carry
        result += str(current % 2)  # get binary value between 0, 1, 2 and 3
        carry = current // 2  # possible values: 0 or 1
    if carry:
        result += 1

    return result[::-1]


a = "11"
b = "1"
print(addBinary(a, b))
