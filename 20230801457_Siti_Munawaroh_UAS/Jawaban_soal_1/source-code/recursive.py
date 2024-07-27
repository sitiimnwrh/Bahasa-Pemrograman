def factorial(n):
    if n == 0:  # Basis kasus: 0! = 1
        return 1
    else:
        return n * factorial(n - 1)  # Rekursi: n! = n * (n-1)!

print(factorial(6))  # Output: 720
