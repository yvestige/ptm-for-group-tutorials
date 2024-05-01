class SchoolSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name):
        self.students.append(name)
        print(f"Student {name} added successfully.")

    def remove_student(self, name):
        if name in self.students:
            self.students.remove(name)
            print(f"Student {name} removed successfully.")
        else:
            print(f"Student {name} not found.")

    def print_students(self):
        if self.students:
            print("List of Students:")
            for i, student in enumerate(self.students, 1):
                print(f"{i}. {student}")
        else:
            print("No students in the system.")

    def get_num_students(self):
        return len(self.students)


def main():
    school = SchoolSystem()
    while True:
        print("\nSchool System Menu:")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Print Students")
        print("4. Number of Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            school.add_student(name)
        elif choice == '2':
            name = input("Enter student name to remove: ")
            school.remove_student(name)
        elif choice == '3':
            school.print_students()
        elif choice == '4':
            print("Number of students:", school.get_num_students())
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
