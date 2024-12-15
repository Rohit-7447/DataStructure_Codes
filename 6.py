#Using Linked List
class Node:
    def __init__(self,order_id,customer_name,items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = items
        self.next = None
    
class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def is_empty(self):
        return self.front is None
        
    def add_order(self):
        order_id = int(input("Enter order ID: "))
        customer_name = input("Enter customer name: ")
        items = []
        
        while True:
            choice = int(input("1.Add Item\n2.Done"))
            if choice == 1:
                item = input("Enter item name: ")
                items.append(item)
            elif choice == 2:
                break
            else:
                print("Invalid choice! Try again")
                
        new_order = Node(order_id,customer_name,items)
        
        if self.is_empty():
            self.front = self.rear = new_order
            self.rear.next = self.front
        else:
            self.rear.next = new_order  #link the new node to the rear
            self.rear = new_order           # making the new node as the rear
            self.rear.next = self.front         #updating/linking the new rear.next to self.front
            
        print("Order placed successfully.")
    
    def remove_order(self):
        if self.is_empty():
            print("Queue is empty.")
        elif self.front == self.rear:
            removed_item = self.front
            self.front = None
            self.rear = None
        else:
            removed_item = self.front
            self.front = self.front.next
            self.rear.next = self.front
        print(f"Order from {removed_item.customer_name} removed successfully.")
    
    
    def display_orders(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            while current:
                print(f"Order ID: {current.order_id}, Customer Name: {current.customer_name}, Items : {current.items}")
                if current == self.rear:
                    break
                current = current .next
            print("End of the list.")
            
if __name__=="__main__":
    cq = CircularQueue()
    
    while True:
        print("Welcom to the Drive thru: \n1.Add Order\n2.Remove Order\n3.Display Orders\n4.Exit")
        choice = int(input("Enter your choice"))
        if choice == 1:
            cq.add_order()
        elif choice == 2:
            cq.remove_order()
        elif choice == 3:
            cq.display_orders()
        elif choice == 4:
            print("Exiting .....")
        else:
            print("Invalid choice Enter valid choice")



#Using list
class Orders:
    def __init__(self,capacity):
        self.capacity = capacity
        self.queue = [None]*capacity
        self.front = -1
        self.rear = -1
        
    def is_full(self):
        return (self.rear+1)%self.capacity == self.front
        
    def is_empty(self):
        return self.front == -1
        
    def add_order(self):
        if self.is_full():
            print("Order queue is full!! Can't add more orders")
            return
        order_id = int(input("Enter Order ID: "))
        name = input("Enter Customer name: ")
        
        items = []
        
        while True:
            choice = int(input("1.Add item\n2.Done\nEnter choice: "))
            if choice ==1:
                item = input("Enter item name")
                items.append(item)
            elif choice ==2:
                break
            else:
                print("Enter a valid choice")
                
        order = {"id":order_id,"name":name,"items":items}
        
        #Add the order to the circular queue
        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear+1)%self.capacity
            
        self.queue[self.rear] = order
        print("Order added successfully")
        
    def remove_order(self):
        if self.is_empty():
            print("No orders to remove")
            return
        order = self.queue[self.front]
        print(f"Order from {order['name']} has been removed")
        #remove the order
        
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front +1)%capacity
            
    def display_orders(self):
        if self.is_empty():
            print("No orders in the queue.")
            return
        print("Orders in the queue: ")
        current = self.front
        while True:
            order = self.queue[current]
            print(f"Order ID: {order['id']}")
            print(f"Customer name:  {order['name']}")
            print(f"Items: {',',join(order['items'])}")
            print("------")
            
            if current == self.rear:
                break
            current = (current+1)%self.capacity
        print("End of Order List.\n")
        
if __name__ == "__main__":
    print("Welcome to our Restaurant!")
    capacity = int(input("Enter the max no of orders the queue can hold."))
    orders_queue = Orders(capacity) #object creation and passing the parameter capacity
    
    while True:
        choice = int(input("\n1.Add Order\n2.Remove Order\n3.Display Orders\n4.Exit"))
        if choice == 1:
            orders_queue.add_order()
        elif choice == 2:
            orders_queue.remove_order()
        elif choice == 3:
            orders_queue.display_orders()
        elif choice == 4:
            print("Exiting ....")
            break
        else:
            print("Invalid choice")