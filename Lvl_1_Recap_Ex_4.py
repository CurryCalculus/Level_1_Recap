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
else:
    print("No student data entered.")
