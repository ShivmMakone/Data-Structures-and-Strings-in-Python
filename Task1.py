def stud():
    """Creates a dictionary of student marks, retrieves and displays marks."""

    student_data = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 95,
    }
    stud_name = input("Enter the student's name: ")

    if stud_name in student_data:
        print(f"{stud_name}'s marks: {student_data[stud_name]}")
    else:
        print("Student not found.")

if __name__ == "__main__":
    stud()