a, b = input().split()
a = int("".join(reversed(a)))
b = int("".join(reversed(b)))

result = a if a > b else b
print(result)