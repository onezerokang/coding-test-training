n = int(input())
people = list(map(int, input().split()))
people.sort(reverse=True)

result = 0
for i in range(len(people)):
    result += people[i] + sum(people[i + 1:])

print(result)
