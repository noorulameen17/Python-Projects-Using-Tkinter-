
class ATM:
    def __init__(self):
        self.balance = 100  # initial balance
        self.transactions = []
        self.accounts = {
            "123456": {"pin": "7890", "balance": 10000},
            "995259": {"pin": "2004", "balance": 15000},
            "842828": {"pin": "1212", "balance": 20000},
            
        }
        self.current_user = None

    def login(self):
        print("\n\t\t\tHELLO CUSTOMER!")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")

        if user_id in self.accounts and self.accounts[user_id]["pin"] == pin:
            self.current_user = user_id
            self.balance = self.accounts[user_id]["balance"]
            print("\n\t\tLogin successful!")
        else:
            print("\nInvalid user ID or PIN. Please try again.")

    def display_menu(self):
        print("\n\t\tWelcome to <ATM 24> ")
        print("\t")
        print("1. Transactions History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Quit")

    def show_transactions(self):
        print("\nTransaction History:")
        for transaction in self.transactions:
            print(transaction)

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"\n\tWithdrawn: ₹{amount}")
            print(f"\n₹{amount} withdrawn successfully.")
        else:
            print("\nInsufficient Funds.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"\n\tDeposited: ₹{amount}")
            print(f"\n₹{amount} deposited successfully.")
        else:
            print("\nInvalid amount.")

    def transfer(self, amount):
        if amount > 0 and amount <= self.balance:
            recipient = input("\nEnter Recipient's account number: ")
            self.balance -= amount
            self.transactions.append(f"\n Amount Transferred: ₹{amount} <To> Account Number: {recipient}")
            print(f"\n₹{amount} Amount Transferred Successfully <To> Account Number: {recipient}.")
        else:
            print("\nInsufficient Funds.")

    def run(self):
        while True:
            if not self.current_user:
                self.login()

            if self.current_user:
                self.display_menu()
                print("\t\t\tDEAR CUSTOMER!")
                choice = input("\nPlease Select Your Transaction: ")

                if choice == '1':
                    self.show_transactions()
                elif choice == '2':
                    amount = float(input("\nEnter Amount To Withdraw: ₹"))
                    self.withdraw(amount)
                elif choice == '3':
                    amount = float(input("\nEnter Amount To Deposit: ₹"))
                    self.deposit(amount)
                elif choice == '4':
                    amount = float(input("\nEnter Amount To Transfer: ₹"))
                    self.transfer(amount)
                elif choice == '5':
                    print("\nThanks for using ATM 24! ")
                    break
                else:
                    print("\n\t\t   !ERROR!")
                    print("\t\tInvalid choice")


# Create an instance of the ATM class and run the ATM interface
if __name__ == "__main__":
    atm = ATM()
    atm.run()
