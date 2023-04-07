c = int(input())

for i in range(c):
    score_list = input().split()
    student_count = int(score_list[0])
    total_score = 0

    for i in range(1, student_count + 1):
        total_score += int(score_list[i])
    
    average = total_score / student_count
    
    good_student_count = 0
    for i in range(1, student_count + 1):
        if int(score_list[i]) > average:
            good_student_count += 1
    
    print(format(good_student_count / student_count * 100, '.3f'), "%", sep="")
    
