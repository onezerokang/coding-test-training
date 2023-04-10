n = int(input())

# 방법1: 문자열을 뒤집어서 같은지 확인한다.

for i in range(n):
    s = input().lower()
    size = len(s)
    if s == s[::-1]:
        print('#%d YES' %(i+1))
    else:
        print('#%d NO' %(i+1))

# 방법2: 재귀함수를 이용해 앞 뒤 글자가 같은지 확인한다.

def get_first_letter(word):
    return word[0:1]

def get_last_letter(word):
    return word[len(word) - 1:]


def get_mid_letter(word):
    return word[1:len(word) - 1]


def check_palindrome(word, i):
    word = word.lower()
    size = len(word)
    if size == 0 or size == 1:
        print(f"#{i} YES")
        return

    first = get_first_letter(word)
    last = get_last_letter(word)

    if first != last:
        print(f"#{i} NO")
        return

    check_palindrome(get_mid_letter(word, i))

for i in range(n):
    word = input()
    check_palindrome(word, i)

