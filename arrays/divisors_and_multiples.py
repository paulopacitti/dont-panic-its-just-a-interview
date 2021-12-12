# description: https://www.geeksforgeeks.org/count-the-number-of-pairs-i-j-such-that-either-arri-is-divisible-by-arrj-or-arrj-is-divisible-by-arri/

def divisors_and_multiples(array):
    pairs = set()
    for i in range(len(array)):
        for j in range(i, len(array)):
            if i != j and (array[i]%array[j] == 0 or array[j]%array[i] == 0):
                if (j, i) not in pairs:
                    pairs.add((i,j)) 
    return pairs

a = [3, 2, 4, 2, 6]
print(divisors_and_multiples(a))

# Time complexity: O(n²)
# Space complexity: O(n²)