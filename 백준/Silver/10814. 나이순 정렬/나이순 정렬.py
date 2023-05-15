import sys
input = sys.stdin.readline

N = int(input())
users = []
for i in range(N):
    age, name = input().rstrip().split()
    users.append((int(age), i, name))
users.sort(key=lambda x: (x[0], x[1]))

for user in users:
    print(user[0], user[2])