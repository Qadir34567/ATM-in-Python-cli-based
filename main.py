class ATM:
    def __init__(self):
        self.balance = 5000
        self.pin = 1234

    def check_pin(self, input_pin):
        return input_pin == self.pin

    def check_balance(self):
        print(f"Your current balance is: Rs. {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        pin = int(input("Enter your PIN to confirm deposit: "))
        if self.check_pin(pin):
            self.balance += amount
            print(f"Rs. {amount} deposited successfully.")
        else:
            print(f"Incorrect PIN. Deposit failed.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        pin = int(input("Enter your PIN to confirm withdrawal: "))
        if self.check_pin(pin):
            if amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"Rs. {amount} withdrawn successfully.")
        else:
            print("Incorrect PIN. Withdrawal failed.")

    def exit(self):
        print("Thank you for using the ATM. Goodbye!")
        quit()

    def run(self):
        while True:
            print("\n===== ATM MENU =====")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.check_balance()
            elif choice == "2":
                try:
                    amount = float(input("Enter amount to deposit: Rs. "))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid input. Enter numeric value.")
            elif choice == "3":
                try:
                    amount = float(input("Enter amount to withdraw: Rs. "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input. Enter numeric value.")
            elif choice == "4":
                self.exit()
            else:
                print("Invalid choice. Please select from 1 to 4.")


atm = ATM()
atm.run()
