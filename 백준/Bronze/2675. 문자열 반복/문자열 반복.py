t = int(input())

for i in range(t):
    r, s = input().split()
    result = ""
    for letter in s:
        result += letter * int(r)
    print(result)