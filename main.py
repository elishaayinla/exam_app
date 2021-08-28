# this is a program that calculates the total score for a students result
# when line 16 is in line 14 it says "this code is unreachable"
# Line 16 displays before the RETRUN code in line 13, WHY? It is supposed to be the reverse
#Enter first test score
#Enter exam score
e_score = input("Enter your exam score!\n")
exam = int(e_score)
test = 30

def check_exam(exam_score):
    print (f"{test+exam_score}")
check_exam(exam)