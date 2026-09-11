"""
python banking program

1. show balance
2. Deposit
3. Withdraw
4. Exit
"""
    
def show_balance(balance):
    print("*****************")
    print(f"Your balance is ${balance:.2f}")
    print("*****************")
    return 0

def deposit():
    amount = float(input("Enter the amount to be deposited ($): "))
    if amount <= 0:
        print("*****************")
        print("Amount nust be greater than 0")
        print("*****************")
        return 0
    else:
        print("*****************")
        print(f"${amount:.2f} has been deposited")
        print("*****************")
        return amount
    

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw ($): "))
    if amount > balance:
        print("*****************")
        print("Insufficient balance")
        print("*****************")
        return 0
    elif amount < 0:
        print("*****************")
        print("Amount must be greater than 0")
        print("*****************")
        return 0
    else:
        print("*****************")
        print(f"{amount:.2f} has been withdrawn")
        print("*****************")
        return amount

def main():    
    balance = 0
    is_running = True
        
    while is_running:
        print("*****************")
        print("Banking Program")
        print("*****************")
        
        print("Select 1 to Show balance")
        print("Select 2 to Deposit")
        print("Select 3 to Withdraw")
        print("Select 4 to Exit")
        print("*****************")
        
        choice = input("Select a service: ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice, try again")
            print("*****************")
            
    print("Thank you for banking with us, have a great day!")
    print("*****************")
        
if __name__ == "__main__":
    main()