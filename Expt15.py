# Implementation of Stack (One Storage Allocation Strategy)

SIZE = 5


class Stack:
    def __init__(self):
        self.s = []
        self.top = -1

    def is_full(self):
        return self.top >= SIZE - 1

    def is_empty(self):
        return self.top == -1

    def push(self, item):
        if self.is_full():
            print("\nStack is Full!")
        else:
            self.s.append(item)
            self.top += 1

    def pop(self):
        if self.is_empty():
            print("\nEmpty stack! Underflow!!")
        else:
            item = self.s.pop()
            self.top -= 1
            print(f"\nThe popped element is {item}")

    def display(self):
        if self.is_empty():
            print("\nStack is Empty!")
        else:
            print("\nStack elements are:")
            for i in range(self.top, -1, -1):
                print(self.s[i])


# Main Program
stack = Stack()

print("\n\tImplementation Of Stack")

while True:
    print("\nMain Menu")
    print("1.Push \n2.Pop \n3.Display \n4.Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        item = int(input("Enter the item to be pushed: "))
        stack.push(item)

    elif choice == 2:
        stack.pop()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        break

    else:
        print("Invalid Choice!")

    ans = input("\nDo You want To Continue? (y/n): ")
    if ans.lower() != 'y':
        break
