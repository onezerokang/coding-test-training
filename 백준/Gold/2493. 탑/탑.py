import sys
input = sys.stdin.readline
n = int(input())
tops = list(map(int, input().split()))

stack = [] # 0: 탑 높이, 1: 인덱스
result = [] 

for i, top in enumerate(tops):
    # 자신보다 작은 탑을 pop함
    while stack and top >= stack[-1][0]:
        stack.pop()
    
    if not stack:
        result.append(0)
    else:
        result.append(stack[-1][1])
    stack.append([top, i + 1])

for num in result:
    print(num, end=' ')