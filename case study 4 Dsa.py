def addtray(stack):
    if len (stack) ==30:
        print("Stack is full")
    else:
        tray = input("Enter the tray name: ")
        if tray in stack:
            print("Tray already exists in the stack")
        else:
            clean = input("Is the tray clean? (yes/no): ")
            damaged = input("Is the tray damaged? (yes/no): ")

            if clean.lower() == "yes" and damaged.lower() == "no":
                stack.append(tray)
                print(f"Tray '{tray}' added to the stack.")
            else:
                print("Tray cannot be added. ")



def removetray(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Removed tray:", stack.pop())

def peekTray(stack):
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Top tray:", stack[-1])

stack = []

while True:
    print("\nMenu:")
    print("1. Add Tray")
    print("2. Remove Tray")
    print("3. Top Tray")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == "1":
        addtray(stack)
    elif choice == "2":
        removetray(stack)
    elif choice == "3":
        peekTray(stack)
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")