n = int(input())
def hanoi(n, curr, goal):
    if n < 1:
        return

    hanoi(n - 1, curr, 6 - curr - goal)
    print(curr, goal)
    hanoi(n - 1, 6 - curr - goal, goal)
    
print(2 ** n - 1)
hanoi(n, 1, 3)