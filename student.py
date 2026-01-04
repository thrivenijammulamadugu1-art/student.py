import json
import os

FILE_NAME = "students.json"

class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "grade": self.grade
        }

class StudentManager:
    def __init__(self):
        self.students = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as f:
                self.students = json.load(f)

    def save_data(self):
        with open(FILE_NAME, "w") as f:
            json.dump(self.students, f, indent=4)

    def add_student(self):
        sid = input("Enter ID: ")
        if sid in self.students:
            print("ID already exists")
            return
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        student = Student(sid, name, grade)
        self.students[sid] = student.to_dict()
        self.save_data()
        print("Student Added")

    def update_student(self):
        sid = input("Enter ID: ")
        if sid not in self.students:
            print("Student not found")
            return
        self.students[sid]["name"] = input("New Name: ")
        self.students[sid]["grade"] = input("New Grade: ")
        self.save_data()
        print("Student Updated")

    def delete_student(self):
        sid = input("Enter ID: ")
        if sid in self.students:
            del self.students[sid]
            self.save_data()
            print("Student Deleted")
        else:
            print("Student not found")

    def list_students(self):
        print("\nID\tName\tGrade")
        print("-" * 25)
        for s in self.students.values():
            print(f"{s['id']}\t{s['name']}\t{s['grade']}")

def main():
    manager = StudentManager()
    while True:
        print("\n1.Add  2.Update  3.Delete  4.List  5.Exit")
        choice = input("Choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.update_student()
        elif choice == "3":
            manager.delete_student()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
