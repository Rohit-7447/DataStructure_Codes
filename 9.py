#hashing
class StudentRecord:
    def __init__(self,student_id,name,age,major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        
class StudentHashTable:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def hash_function(self,student_id):
        return student_id%self.size
    
    def addStudent(self,student):
        index = self.hash_function(student.student_id)
        for existing_student in self.table[index]:
            if existing_student.student_id == student.student_id:
                print("Student with this ID already exists.")
                return
        self.table[index].append(student)
        print("Student record added successfully.")
  
    def retrieve_student(self,student_id):
        index = self.hash_function(student_id)
        for student in enumerate(table[index]):
            if student.student_id == student_id:
                return student
        return None
            
    
    def delete_student(self,student_id):
        index = self.hash_function(student_id)
        for i, student in enumerate(self.table[index]):
            if student.student_id == student_id:
                del self.table[index][i]
                print("Student record deleted successfully.")
                return
        print("Student record not found.")
    
    def display_all_students(self):
        print("All students record.")
        for index, students in enumerate(self.table):
            for student in students:
                print(student)
                
def main():
    system = StudentHashTable()
    while True:
        print("\nStudent Information System")
        print("1.Add new Student Record")
        print("2.Retrieve Student Information")
        print("3.Delete Student Information")
        print("4.Display Student Record ")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            student_id = int(input("Enter Student Id: "))
            name = input("Enter student's name: ")
            age = int(input("Enter student's age: "))
            major = input("Enter student's major: ")
            student = StudentRecord(student_id,name,age,major)
            system.addStudent(student)
        
        elif choice == 2:
            student_id = input("Enter Student ID: ")
            student = system.retrieve_student(student_id)
            if student:
                print("Student record found: ",student)
            else:
                print("Student record not found.")
                
        elif choice == 3:
            student_id = input("Enter student id:")
            system.delete_student()
            
        elif choice == 4:
            system.display_all_students()
        elif choice == 5:
            print("Exiting .....")
            break
        else:
            print("Invalid choice.")
            
if __name__ == "__main__":
    main()