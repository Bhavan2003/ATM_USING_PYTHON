print('*' * 5, 'Welcome to ATM', '*' * 5)
print("Insert your ATM card\n")

pin = input("Enter your 4-digit PIN: ")

if len(pin) == 4:
    balance = 5000  
    while True:
        print("\n----- ATM Menu -----")
        print("1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print(f"Your balance is: ₹{balance}")
        
        elif choice == "2":
            amount = int(input("Enter withdrawal amount: ₹"))
            if amount > balance:
                print("Insufficient balance!")
            elif amount <= 0:
                print("Enter a valid amount!")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully. Remaining balance: ₹{balance}")
        
        elif choice == "3":
            amount = int(input("Enter deposit amount: ₹"))
            if amount <= 0:
                print("Enter a valid amount!")
            else:
                balance += amount
                print(f"₹{amount} deposited successfully. Current balance: ₹{balance}")
        
        elif choice == "4":
            print("Thank you for using our ATM. Please take your card.")
            break
        
        else:
            print("Invalid choice! Please enter between 1-4.")
else:
    print("Invalid PIN! PIN must be 4 digits.")


      
