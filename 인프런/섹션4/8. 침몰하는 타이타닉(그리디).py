from collections import deque

N, M = map(int, input().split())
people = list(map(int, input().split()))
people.sort()
people = deque(people)
cnt = 0

while people:
    if len(people) == 1:
        cnt +=1
        break
    if M > people[0] + people[-1]:
        people.pop()
        cnt +=1
    else:
        people.pop()
        people.popleft()
        cnt +=2
print(cnt)