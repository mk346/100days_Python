# for loop -> calculating average
student_heights = input("Input a list of student heights: ").split()
# print (type(student_heights))
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# print(student_heights)
total_height = 0
for height in student_heights:
    total_height += height
    average_height = total_height / len(student_heights)
print(round(average_height))





