class Node:    
    def __init__(self, patient_id, name, age, patient_problem):        
        self.patient_id = patient_id        
        self.name = name        
        self.age = age        
        self.patient_problem = patient_problem        
        self.next = None

class LinkedList:    
    def __init__(self):        
        self.head = None
    
    def add(self, patient_id, name, age, patient_problem):        
        new_node = Node(patient_id, name, age, patient_problem)        
        if self.head is None:            
            self.head = new_node        
        else:            
            current = self.head   
            while current.next:                
                current = current.next            
            current.next = new_node

    def search(self, patient_id):        
        current = self.head     
        while current:           
            if current.patient_id == patient_id:                
                return current            
            current = current.next        
        return None  # Moved outside the loop to execute only after the entire list is traversed
        
    def delete(self, patient_id):        
        current = self.head        
        prev = None        
        while current and current.patient_id != patient_id:            
            prev = current            
            current = current.next
        
        if current is None:  # Node with patient_id not found
            print(f"Patient ID {patient_id} not found")
            return
        
        if prev is None:  # Deleting the head node
            self.head = current.next
        else:  # Bypassing the node to delete
            prev.next = current.next
        
        print(f"Patient ID {patient_id} deleted successfully")

    def move_to_front(self, patient_id):        
        if self.head is None:  # Empty list
            print(f"List is empty. Cannot move patient ID {patient_id}.")
            return
        
        if self.head.patient_id == patient_id:  # Already at front
            print(f"Patient with ID {patient_id} is already at the front.")
            return
        
        current = self.head        
        prev = None
        while current and current.patient_id != patient_id:            
            prev = current            
            current = current.next
        
        if current is None:  # Node not found
            print(f"Patient with ID {patient_id} not found.")
            return
        
        # Move to front
        if prev:
            prev.next = current.next
        current.next = self.head        
        self.head = current        
        print(f"Patient with ID {patient_id} has been moved to front.")

    def display(self):        
        current = self.head        
        if not current:
            print("No patients in the list.")
            return
        
        while current:            
            print(f"ID: {current.patient_id}, Name: {current.name}, Age: {current.age}, Problem: {current.patient_problem}", end=' ► ')
            current = current.next
        print("None")

class HospitalManagementSystem:    
    def __init__(self):  # Default constructor       
        self.list = LinkedList()  # Object creation of linked list class
    
    def menu(self):        
        while True:            
            print("Welcome to Hospital Management System")            
            print("1. Add patient\n2. Search patient by ID\n3. Delete patient by ID\n4. Move patient to front\n5. Display all patients\n6. Exit")
            choice = int(input("Enter your choice: "))                    
            if choice == 1:                
                self.addy()            
            elif choice == 2:                
                self.search_p()            
            elif choice == 3:                
                self.delete_p()            
            elif choice == 4:                
                self.moveto_front()            
            elif choice == 5:                
                self.list.display()            
            elif choice == 6:
                print("Program Exited Successfully")                
                break            
            else:                
                print("Invalid input")
    
    def addy(self):        
        patient_id = int(input("Patient ID: "))        
        name = input("Name: ")        
        age = int(input("Age: "))        
        patient_problem = input("Patient problem: ")        
        self.list.add(patient_id, name, age, patient_problem)        
        print("Patient added successfully.")
    
    def search_p(self):        
        patient_id = int(input("Enter the patient ID: "))        
        patient = self.list.search(patient_id)        
        if patient:            
            print(f"Patient found: ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}, Problem: {patient.patient_problem}")        
        else:            
            print(f"Patient with ID {patient_id} not found.")

    def delete_p(self):        
        patient_id = int(input("Enter the patient ID: "))        
        self.list.delete(patient_id)
    
    def moveto_front(self):        
        patient_id = int(input("Enter patient ID: "))        
        self.list.move_to_front(patient_id)

if __name__ == "__main__":    
    h = HospitalManagementSystem()    
    h.menu()
