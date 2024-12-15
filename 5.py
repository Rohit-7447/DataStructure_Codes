#rk-method
class Node:
    def __init__(self,name,id,service):
        self.name = name
        self.id = id
        self.service = service
        self.next = None
        
class List:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def addService(self):
        id = int(input("Request ID: "))
        name = input("Customer Name: ")
        service = input("Service Type: ")
        newnode = Node(name,id,service)

        if self.front == None and self.rear == None:
            self.front = newnode
            self.rear = newnode
            return
        else:
            self.rear.next = newnode
            self.rear = newnode
            return
        
    def removeService(self):
        if self.front == None and self.rear == None:
            print("Queue is empty")
        elif self.front == self.rear:
            temp = self.front
            self.front = None
            self.rear = None
            print(f"{temp.name} is successfully removed from list.")
            return    
        else:
            temp = self.front
            self.front = self.front.next
            print(f"{temp.name} is successfully removed from the list.")
            return
        
    def display(self):
        if self.front == None and self.rear == None:
            print("Queue is empty")
            return
        current = self.front
        while current:
            print(f"Customer ID: {current.id},Customer name: {current.name},Service Type: {current.service}")
            current = current.next
    
if __name__ == "__main__":
    list = List()
    
    print("Welcome to Call center")
    
    while True:
        print("1.Add customer\n2.Remove Customer\n3.Display Customer\n4.Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            list.addService()
            
        elif choice == 2:
            list.removeService()
            
        elif choice == 3:
            list.display()
            
        elif choice == 4:
            print("Exiting ....")
            break
            
        else:
            print("Invalid choice, Try again")

#mm-method
class customer:
    def __init__(self, name, contact_info , service ):
        self.name = name
        self.contact_info = contact_info
        self.service = service
        self.status = "Pending"
        self.next = None


class CustomerService:
    def __init__(self):
        self.head = None

    def add_customer(self, name, contact_info, service):


        if self.head is None:
            self.head = customer(name, contact_info, service)
            return

        current = self.head
        while current.next:
            current=current.next

        new_customer = customer(name, contact_info, service)
        current.next = new_customer

    def process_current_customer(self):
        if self.head is None:
            return None
        self.head.status = "In Progress"
        return self.head

    def complete_current_customer(self):
        if self.head is None:
            return None
        removed_customer = self.head
        removed_customer.status = "Completed"
        self.head = self.head.next
        return removed_customer

    def display_customer_by_status(self):
        statuses = {"Pending": [], "In Progress": [], "Completed": []}
        current = self.head
        while current:
            statuses[current.status].append(current.name)
            current = current.next
        for status, customers in statuses.items():
            if customers:
                print(f"Customers With {status} Status")
                for customer in customers:
                    print(f"   -Customer : {customer}")





service = CustomerService()

service.add_customer("Customer 1", "1234567890", "Service 1")
service.add_customer("Customer 2", "0987654321", "Service 2")
service.add_customer("Customer 3", "6789054321", "Service 3")

print("Customers in service:")
service.display_customer_by_status()

print("\nProcessing current customer...")
service.process_current_customer()

print("Customers in service after processing:")
service.display_customer_by_status()

print("\nCompleting current customer...")
service.complete_current_customer()

print("Customers in service after completion:")
service.display_customer_by_status()