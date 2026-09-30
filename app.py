print("===== PocketSmart AI =====")

name = input("Enter your name: ")
budget = float(input("Enter your monthly budget: "))
expense = float(input("Enter your total expenses: "))

balance = budget - expense

print("\n----- Budget Summary -----")
print("Name:", name)
print("Monthly Budget: ₹", budget)
print("Total Expenses: ₹", expense)
print("Remaining Balance: ₹", balance)

if balance > 0:
    print("Recommendation: You are within your budget.")
    print("You can save ₹", balance)
elif balance == 0:
    print("Recommendation: You have used your full budget.")
else:
    print("Recommendation: You have exceeded your budget.")
    print("Extra amount spent: ₹", abs(balance))

print("\nThank you for using PocketSmart AI!")
