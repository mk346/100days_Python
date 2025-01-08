student_marks = input("Input a list of student marks: ").split()
# print (type(student_heights))
for n in range(0, len(student_marks)):
    student_marks[n] = int(student_marks[n])
# print(student_marks)
print(min(student_marks))
# for mark in student_marks:
#     print(mark)