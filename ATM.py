class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        if input_pin == self.pin:
            return True
        else:
            print("Invalid PIN.")
            return False

    def check_balance(self):
        print(f"Your current balance is: Rs {self.balance}")

    def deposit(self, input_pin, amount):
        if not self.check_pin(input_pin):
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Rs {amount} deposited successfully.")
        self.check_balance()

    def withdraw(self, input_pin, amount):
        if not self.check_pin(input_pin):
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient balance.")
            return
        self.balance -= amount
        print(f"Rs {amount} withdrawn successfully.")
        self.check_balance()

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        quit()


# Example usage
atm = ATM()

while True:
    print("\n----- ATM Menu -----")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        atm.check_balance()

    elif choice == '2':
        pin = int(input("Enter PIN: "))
        amount = int(input("Enter amount to deposit: "))
        atm.deposit(pin, amount)

    elif choice == '3':
        pin = int(input("Enter PIN: "))
        amount = int(input("Enter amount to withdraw: "))
        atm.withdraw(pin, amount)

    elif choice == '4':
        atm.exit()

    else:
        print("Invalid choice. Please select 1-4.")