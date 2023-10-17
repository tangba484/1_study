import math
def solution(n, k):
    numbers = list(range(1, n + 1))
    result = []
    
    k -= 1
    
    for i in range(1, n + 1):
        f = math.factorial(n - i)
        index = k // f
        result.append(numbers[index])
        numbers.pop(index)
        k %= f
    
    return result
