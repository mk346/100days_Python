# grading
student_marks = {
    "Caleb": 87,
    "Harris": 65,
    "Ann": 92,
    "Micheal": 55,
    "John": 78,
    "Angela": 42,
}

student_grades = {}

for student in student_marks:
    if student_marks[student] > 90:
        student_grades[student] = "Excellent"
    elif student_marks[student] >= 80:
        student_grades[student] = "Very Good"
    elif student_marks[student] >= 60:
        student_grades[student] = "Good"
    else:
        student_grades[student] = "Poor"

print(student_grades)