import csv
import os

FILE_NAME = "students.csv"


# Create CSV file if it doesn't exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Roll Number", "Name", "Marks"])


# Add student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, marks])

    print("Student added successfully!")


# Display all students
def display_students():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        data = list(reader)

    if len(data) <= 1:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for row in data:
        print(f"Roll Number: {row[0]} | Name: {row[1]} | Marks: {row[2]}")


# Search student
def search_student():
    roll = input("Enter Roll Number to search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        found = False

        for student in reader:
            if student["Roll Number"] == roll:
                print("\nStudent Found!")
                print("Roll Number:", student["Roll Number"])
                print("Name:", student["Name"])
                print("Marks:", student["Marks"])
                found = True
                break

        if not found:
            print("Student not found.")


# Delete student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    students = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if student["Roll Number"] != roll:
                students.append(student)

    found = len(students) < get_student_count()

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            fieldnames = ["Roll Number", "Name", "Marks"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully!")
    else:
        print("Student not found.")


# Count students
def get_student_count():
    count = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            count += 1

    return count


# Main program
def main():
    create_file()

    while True:
        print("\n==============================")
        print("   STUDENT MANAGEMENT SYSTEM")
        print("==============================")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


main()
