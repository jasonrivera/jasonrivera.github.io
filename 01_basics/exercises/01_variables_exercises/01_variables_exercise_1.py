"""
Exercise: 
Personal Budget Tracker

Scenario: 
Imagine you are managing your monthly budget. You want to keep track of your income and expenses to see how much money you have left at the end of the month.

Objective: 
Write a simple Python script to calculate your remaining budget after accounting for various expenses.

Instructions:

1. Define Variables:
   - Create a variable `monthly_income` and assign it a value representing your total income for the month.
   - Create variables for different types of expenses:
     - `rent`
     - `groceries`
     - `utilities`
     - `transportation`
     - `entertainment`

2. Assign Values:
   - Assign realistic values to each of these variables based on your hypothetical budget.

3. Calculate Total Expenses:
   - Create a variable `total_expenses` that sums up all the expense variables.

4. Calculate Remaining Budget:
   - Create a variable `remaining_budget` that calculates the difference between `monthly_income` and `total_expenses`.

5. Output the Results:
   - Print out each expense category and its value.
   - Print the `total_expenses`.
   - Print the `remaining_budget`.



Goals:

- Understand Variables: Practice creating and using variables to store data.
- Basic Arithmetic: Use arithmetic operations to calculate totals and differences.
- Output: Learn how to print and format output to display information clearly.

This exercise will help you understand how variables can be used to model real-world scenarios and perform basic calculations.
"""

# monthly income variable
monthly_income = 6000

# expense variables
rent = 1700
groceries = 1200
utilities = 600
transportation = 250
entertainment = 500


# calculate total expenses
total_expenses = rent + groceries + utilities + transportation + entertainment


# remaining budget variable
remaining_budget = monthly_income - total_expenses


# print out each expense category and its value
print(f"Rent is: ${rent}/month.")
print(f"Groceries is: ${groceries}/month.")
print(f"Utilities is: ${utilities}/month.")
print(f"Transportation is: ${transportation}/month.")
print(f"Entertainment is: ${entertainment}/month.")

# print total expenses
print(f"Total expenses is: {total_expenses}/month.")

# print remaining budget
print(f"Remaining budget is: {remaining_budget}/month.")

# Below is the output:
# Rent is: $1700/month.
# Groceries is: $1200/month.
# Utilities is: $600/month.
# Transportation is: $250/month.
# Entertainment is: $500/month.
# Total expenses is: 4250/month.
# Remaining budget is: 1750/month.