
import sys
T = int(sys.stdin.readline())
cnt = 0
def check_palindrome(string):
    global cnt
    cnt += 1
    if len(string) <= 1:
        print(1, cnt)
        cnt = 0
        return
    if string[0] != string[-1]:
        print(0, cnt)
        cnt = 0
        return

    return check_palindrome(string[1:-1])


for _ in range(T):
    string = sys.stdin.readline().rstrip()
    check_palindrome(string)
