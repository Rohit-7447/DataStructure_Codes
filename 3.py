class Node:
    def __init__(self, product_id, name, quantity, price):
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.prev = None
        self.next = None


class Inventory:
    def __init__(self):
        self.head = None

    def additem(self, product_id, name, quantity, price):
        newnode = Node(product_id, name, int(quantity), float(price))
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newnode
            newnode.prev = current

    def deleteitem(self, product_id):
        if self.head is None:
            print("List is Empty")
        else:
            current = self.head
            while current and current.product_id != product_id:
                current = current.next

            if current is None:
                print("Item not found.")
                return

            if current == self.head:
                self.head = current.next
                if self.head:
                    self.head.prev = None
            elif current.next is None:  # If it's the tail node
                current.prev.next = None
            else:
                current.prev.next = current.next
                current.next.prev = current.prev

            print(f"Deleted item with Product ID: {product_id}")

    def updateitem(self, product_id, up_quantity):
        if self.head is None:
            print("List is Empty")
        else:
            current = self.head
            while current and current.product_id != product_id:
                current = current.next

            if current is None:
                print("Item not found.")
                return

            if current.quantity == int(up_quantity):
                print("No need to update quantity.")
            else:
                current.quantity = int(up_quantity)
                print(f"Updated quantity of Product ID: {product_id} to {up_quantity}")

    def search(self, product_id):
        if self.head is None:
            print("List is Empty.")
        else:
            current = self.head
            while current and current.product_id != product_id:
                current = current.next

            if current is None:
                print("Item not found.")
                return

            print(f"Item found\nProduct ID: {current.product_id}\nProduct Name: {current.name}\nProduct Quantity: {current.quantity}\nProduct Price: {current.price}\nProduct Amount: {current.price * current.quantity}\n")

    def calculatetotalvalue(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            total_value = 0
            while current:
                total_value += current.price * current.quantity
                current = current.next
            print(f"Total Inventory Value is {total_value}")

    def displayallproducts(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(f"Product ID: {current.product_id}\nProduct Name: {current.name}\nProduct Quantity: {current.quantity}\nProduct Price: {current.price}\nProduct Amount: {current.price * current.quantity}\n", end="")
                current = current.next
            print("None")


if __name__ == "__main__":
    iv = Inventory()
    while True:
        print("\nEnter to Inventory Management System")
        print("1. Add Item to Inventory\n2. Delete Item from Inventory\n3. Update item quantity\n4. Search for Item\n5. Display all items\n6. Calculate total value of Inventory\n7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            quantity = input("Enter product quantity: ")
            price = input("Enter product price: ")
            iv.additem(product_id, name, quantity, price)

        elif choice == 2:
            product_id = input("Enter product ID to delete: ")
            iv.deleteitem(product_id)

        elif choice == 3:
            product_id = input("Enter product ID to update quantity: ")
            up_quantity = input("Enter updated quantity: ")
            iv.updateitem(product_id, up_quantity)

        elif choice == 4:
            product_id = input("Enter the product ID to search: ")
            iv.search(product_id)

        elif choice == 5:
            iv.displayallproducts()

        elif choice == 6:
            iv.calculatetotalvalue()

        elif choice == 7:
            print("Exiting the System")
            break

        else:
            print("Invalid choice")
