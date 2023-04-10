n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

new_list = []

p1 = 0
p2 = 0
while p1 < n and p2 < m:
    if a_list[p1] < b_list[p2]:
        new_list.append(a_list[p1])
        p1 += 1
    else:
        new_list.append(b_list[p2])
        p2 += 1
if p1 < n:
    new_list += a_list[p1:]
if p2 < m:
    new_list += b_list[p2:]
        
for x in new_list:
    print(x, end=" ")