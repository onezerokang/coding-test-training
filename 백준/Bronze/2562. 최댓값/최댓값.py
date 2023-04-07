max_value = 0
index = 0
for i in range(9):
    num = int(input())
    if max_value < num:
        max_value = num
        index = i + 1

print(max_value, index, sep="\n")