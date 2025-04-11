# main.py

from student_manager import StudentManager
from storage import Storage

def display_students(students):
    if not students:
        print("No students found.")
    for s in students:
        print(f"{s.id} - {s.name}, Age: {s.age}, Grade: {s.grade}")

def main():
    manager = StudentManager()
    storage = Storage()

    saved_data = storage.load()
    manager.load_students(saved_data)

    while True:
        print("\n1. Add Student\n2. View All\n3. Search by ID\n4. Delete Student\n5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Name: ")
            age = input("Age: ")
            grade = input("Grade: ")
            student = manager.add_student(name, age, grade)
            storage.save(manager.to_dict_list())
            print(f"Student added with ID: {student.id}")

        elif choice == '2':
            display_students(manager.get_all_students())

        elif choice == '3':
            sid = input("Enter student ID: ")
            student = manager.find_by_id(sid)
            if student:
                print(f"{student.id} - {student.name}, Age: {student.age}, Grade: {student.grade}")
            else:
                print("Student not found.")

        elif choice == '4':
            sid = input("Enter student ID: ")
            if manager.delete_student(sid):
                storage.save(manager.to_dict_list())
                print("Student deleted.")
            else:
                print("Student not found.")

        elif choice == '5':
            print("Exiting.")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
