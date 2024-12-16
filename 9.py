class StudentRecord:
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major


class StudentHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, student_id):
        return student_id % self.size

    def addStudent(self, student):
        index = self.hash_function(student.student_id)
        for existing_student in self.table[index]:
            if existing_student.student_id == student.student_id:
                print("Student with this ID already exists.")
                return
        self.table[index].append(student)
        print("Student record added successfully.")

    def retrieve_student(self, student_id):
        index = self.hash_function(student_id)
        for student in self.table[index]:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        index = self.hash_function(student_id)
        for i, student in enumerate(self.table[index]):
            if student.student_id == student_id:
                del self.table[index][i]
                print("Student record deleted successfully.")
                return
        print("Student record not found.")

    def display_all_students(self):
        print("All student records:")
        for index, students in enumerate(self.table):
            for student in students:
                print(
                    f"Student ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Major: {student.major}"
                )


def main():
    system = StudentHashTable()
    while True:
        print("\nStudent Information System")
        print("1. Add New Student Record")
        print("2. Retrieve Student Information")
        print("3. Delete Student Information")
        print("4. Display All Student Records")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Student's Name: ")
                age = int(input("Enter Student's Age: "))
                major = input("Enter Student's Major: ")
                student = StudentRecord(student_id, name, age, major)
                system.addStudent(student)
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == 2:
            try:
                student_id = int(input("Enter Student ID: "))
                student = system.retrieve_student(student_id)
                if student:
                    print(
                        f"Student Found: ID: {student.student_id}, Name: {student.name}, Age: {student.age}, Major: {student.major}"
                    )
                else:
                    print("Student record not found.")
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == 3:
            try:
                student_id = int(input("Enter Student ID: "))
                system.delete_student(student_id)
            except ValueError:
                print("Invalid input. Please try again.")

        elif choice == 4:
            system.display_all_students()

        elif choice == 5:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()