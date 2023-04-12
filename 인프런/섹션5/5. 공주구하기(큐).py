# deque를 사용해서 푼 코드

from collections import deque
n, k = map(int, input().split())
dq = list(range(1, n + 1))
dq = deque(dq)

while dq:
    for _ in range(k-1):
        curr = deque.popleft()
        deque.append(curr)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()


# 처음 내가 푼 코드
# import queue

# n, k = map(int, input().split())
# q = queue.Queue()

# for i in range(1, n + 1):
#     q.put(i)

# while q.qsize() != 1:
#     for i in range(1, q.qsize() + 2):
#         prince = q.get()
#         if i == k:
#             break
#         q.put(prince)

# print(q.get())