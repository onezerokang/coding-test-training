t = int(input())

for i in range(t):
    n, s, e, k = map(int, input().split())
    num_list = list(map(int, input().split()))
    # s부터 e까지 오름차순정렬
    num_list = num_list[s-1:e]
    num_list.sort()

    print(num_list[k - 1])