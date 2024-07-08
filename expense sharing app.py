from collections import defaultdict

def input_expenses():
    expenses = defaultdict(float)
    while True:
        person_name = input("Enter Name Of The Person (or 'exit' To Finish): ")
        if person_name == "exit":
            break
        description = input("Enter Expense (or 'exit' To Finish): ")
        amount = float(input("Enter Amount: "))
        expenses[(person_name, description)] += amount
    return expenses


def split_bills_equally(expenses, num_people):
    balances = defaultdict(float)
    total_amount = sum(expenses.values())
    individual_share = total_amount / num_people
    for (person, _), amount in expenses.items():
        balances[person] += amount - individual_share
    return balances


def track_owe(balances):
    for person, balance in balances.items():
        if balance > 0:
            print(f"{person} Is Owed {balance}")
        elif balance < 0:
            print(f"{person} Owes {-balance}")
        else:
            print(f"{person} Owes Nothing")

def main():
    expenses = input_expenses()
    num_people = int(input("Enter The Number of People: "))
    balances = split_bills_equally(expenses, num_people)
    track_owe(balances)


if __name__ == "__main__":
    main()
