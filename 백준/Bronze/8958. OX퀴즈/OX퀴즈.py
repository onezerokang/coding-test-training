c = int(input())

def fact(n):
    if n == 1:
        return n
    return n + fact(n - 1)

for i in range(c):
    score = 0
    quiz_result_list = input().split('X')
    for quiz_result in quiz_result_list:
        if quiz_result != '':
            score += fact(len(quiz_result))
    print(score)