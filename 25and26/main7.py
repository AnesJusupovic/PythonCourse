import random

if __name__ == "__main__":
    names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
    student_score = {
        student:random.randint(1, 100) for student in names
    }

    passed_students = {student:student_score.get(student) for student in student_score if student_score.get(student) > 60}
    print(passed_students)