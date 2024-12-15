class Node:
    def __init__(self,task,priority):
        self.task = task
        self.priority = priority
        self.next = None
        
class ToDoList:
    def __init__(self):
        self.head = None
        
    def push(self, task, priority):

#newnode
        newnode = Node(task,priority)
        priority_levels = {"high":1, "medium":2,"low":3}
        
        if self.head is None or priority_levels[priority]<priority_levels[self.head.priority]:
            newnode.next = self.head
            self.head = newnode
        else: #jabtak uska current.next none nahi ho jata yani ki last element ya phir priority level ki condition false nahi ho jati tab tak vo current age badta rahega
            current = self.head
            while current.next is not None and priority_levels[priority]>=priority_levels[current.next.priority]:
                current = current.next
            newnode.next = current.next
            current.next = newnode
            
    def display(self):
        if self.head is None:
            print("No tasks in the list.")
            return
        current = self.head
        while current is not None:
            print(f"Task : {current.task}, Priority: {current.priority}")
            current = current.next
            
    def pop(self):
        if self.head is None:
            print("No task to pop")
            return
        remove_task = self.head
        self.head = self.head.next
        print(f"Popped task:{remove_task.task}, Priority: {remove_task.priority}")
        
    def peek(self):
        if self.head is None:
            print("No tasks in the list.")
            return
        print(f"Task: {self.head.task}, Priority: {self.head.priority}")
        
def main():
    t = ToDoList()
    
    while True:
        print("To Do List Options")
        print("1.Push task in the list")
        print("2.Pop task from the list")
        print("3.Peek task highest priority task")
        print("4.Display all tasks")
        print("5.Exit")
        
        choice = int(input("Enter your choice"))
        if choice ==1:
            task = input("Enter task name:")
            priority = input("Enter the priority (high, medium,low):").lower()
            t.push(task,priority)
            
        elif choice ==2:
            t.pop()
        
        elif choice == 3:
            t.peek()
            
        elif choice == 4:
            t.display()
            
        elif choice == 5:
            print("Exiting ....")
            break
        else:
            print("Invalid choice")
            
if __name__ == "__main__":
    main()