students = []
while True:
    name = input("Enter student name (or 'X' to exit): ")
    if name.upper() == 'X':
        break
    mark = int(input("Enter exam mark (0-100): "))
    students.append((name, mark))

if students:
    best_student = ("", -1)
    total_marks = 0
    for student in students:
        total_marks += student[1]
        if student[1] > best_student[1]:
            best_student = student

    average_mark = total_marks / len(students)
    print(f"Best student: {best_student[0]}, Mark: {best_student[1]}")
    print(f"Average mark: {average_mark}")

    print("\nFollowing are the student's grades:")
    for student in students:
        grade = ""
        if student[1] >= 90:
            grade = "A+"
        elif 85 <= student[1] < 90:
            grade = "A"
        elif 80 <= student[1] < 85:
            grade = "A-"
        elif 75 <= student[1] < 80:
            grade = "B+"
        elif 70 <= student[1] < 75:
            grade = "B"
        elif 65 <= student[1] < 70:
            grade = "B-"
        elif 60 <= student[1] < 65:
            grade = "C+"
        elif 55 <= student[1] < 60:
            grade = "C"
        elif 50 <= student[1] < 55:
            grade = "C-"
        elif 40 <= student[1] < 50:
            grade = "D"
        else:
            grade = "E"

        print(f"{student[0]}'s grade: {grade}")
else:
    print("No student data entered.")
