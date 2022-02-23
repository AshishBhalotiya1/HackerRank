def gradingStudents(grades):
    # Write your code here
    s = ""
    for i in grades:
        if s != "":
            s += "\n"
        if i < 38:
            pass
        elif i % 5 == 3 or i % 5 == 4:
            i = (i//5) * 5 + 5
        s += f"{i}"
    return s


if __name__ == '__main__':
    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    print(result)
