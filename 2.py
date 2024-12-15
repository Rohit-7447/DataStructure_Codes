#mm-method
def subjectAverage(sparse_grades, noOfStudents, noOfGrades):
    subject_totals = [0] * noOfGrades
    subject_counts = [0] * noOfGrades

    for (student, subject), marks in sparse_grades.items():
        subject_totals[subject] += marks
        subject_counts[subject] += 1

    subject_averages = [0] * noOfGrades

    for i in range(0,noOfGrades):
        subject_averages[i]=subject_totals[i]/(1 if subject_counts[i]==0 else subject_counts[i])
    return  subject_averages

def studentAverage(sparse_grades, studentArr , subjectArr):
    student_totals = [0] * len(studentArr)
    student_counts = [0] * len(studentArr)

    for (student, subject), marks in sparse_grades.items():
        student_totals[student] += marks
        student_counts[student] += 1

    student_averages = [0] * len(studentArr)

    for i in range(0,len(studentArr)):
        student_averages[i]=student_totals[i]/(1 if student_counts[i]==0 else student_counts[i])
    return  student_averages


def main():
    grades = [
        [0, 0, 54, 66],
        [85, 0, 0, 0],
        [0, 0, 78, 92],
        [89, 0, 88, 0]
    ]

    noOfStudents = len(grades)
    noOfGrades = len(grades[0])
    studentArr = ["mayank", "pratik", "sagar", "yash"]
    subjectArr = ["maths", "physics", "chemistry", "marathi"]


    sparse_grades = {}
    for i in range(len(grades)):
        for j in range(0,len(grades[i])):
            if grades[i][j] != 0:
                sparse_grades[(i, j)] = grades[i][j]

    print(sparse_grades)

    subject_averages = subjectAverage(sparse_grades,noOfStudents,noOfGrades)
    student_averages = studentAverage(sparse_grades,studentArr,subjectArr)
    

    print(subject_averages)
    print(student_averages)


main()
#Rohit-method
# def subjectAverage(sparse_grades, noOfStudents, noOfGrades):
#     subject_total = [0]*noOfGrades
#     subject_count = [0]*noOfGrades
    
#     for(student,subject),marks in sparse_grade.items():
#         subject_total[subject] += marks
#         subject_count[subject] += 1
    
#     subject_averages = [0]*noOfGrades
#     for i in range(0,noOfGrades):
#         subject_averages[i] = subject_total[i]/(1 if subject_count[i]== 0 else subject_count[i])
#     return subject_averages
    
# def highestScore(sparse_grades, studentArr, subjectArr):
#     highest_scores = {}
#     for (student, subject), marks in sparse_grades.item():
#         subject_name = subjectArr[subject]
#         if subject_name not in highest_scores or marks>highest_scores[subject_name][1]:
#             highest_scores[subject_name] = (studentArr[student], marks)
#     return highest_scores
    
    
# def main():
#     grades = [
#     [0,0,82,56],   #student 1, for subject 0,1,2,3
#     [82,36,0,0],  #student 2 for subject 0-3
#     [0,23,96,0],  #student 3 for subject 0-3
#     [56,0,56,0],  #student 4 for subject 0-3
#     ]
    
#     noOfStudents = len(grades)
#     noOfGrades = len(grades[0])
#     studentArr = ['Mayank',"Rohit","Pratik","Varad"]
#     subjectArr = ["Chemistry","Physics","Maths","Marathi"]
    
#     sparse_grades = {}
    
#     for i in range (len(grades)):
#         for j in range (0, len(grades[0])):
#             if grades[i][j] != 0:
#                 sparse_grade[(i,j)] = grades[i][j]
                
#     print("Sparse_grades : ",sparse_grade)
    
#     subject_averages = subjectAverage(sparse_grades, noOfStudents, noOfGrades)
#     print("Subject Averages : ",subject_averages)