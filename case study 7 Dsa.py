def parkVehicle(stack):
    if len(stack) ==10:
        print("Parking lot is full.")
        return
    vr_no = input("Enter vehicle registration number: ")
    if vr_no in stack:
        print("Vehicle with the same number already exists.")
    else:
        stack.append(vr_no)
        print(f"Vehicle {vr_no} parked successfully.")

def exitVehicle(stack):
    if len(stack) == 0:
        print("Parking lot is empty.")
    else:
        print("Vehicle exited: ", stack.pop())

def topVehicles(stack):
    if len(stack) == 0:
        print("Parking lot is empty.")
    else:
        print("Top vehicle: ", stack[-1])

def displayVehicles(stack):
    if len(stack) == 0:
        print("No vehicles parked.")
    else:
        print("Parked vehicles : ",stack)

stack = []

while True:
    print("\n1. Park Vehicle")
    print("2. Exit Vehicle")
    print("3. Top Vehicle")
    print("4. Display Vehicles")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting the program.")
    vehicle_type = input("Enter vehicle registration number: ")
    if vehicle_type.lower() in ['car', 'bike']:
        if choice == 1:
            parkVehicle(stack)
        elif choice == 2:
            exitVehicle(stack)
        elif choice == 3:
            topVehicles(stack)
        elif choice == 4:
            displayVehicles(stack)
        else:
            print("Invalid choice. Please try again.")
       
        
    else:
        print("You can only park cars and bikes. ")