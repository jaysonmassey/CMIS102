# Assignment 1 - CMIS 102 - Jayson Massey
# The first assignment involves writing a Python program to compute the weekly pay for a salesman.
# Your program should prompt the user for the number of hours worked for that week and the weekly sales.
# Your program should compute the total pay as the sum of the pay based on the number of hours worked times the hourly rate plus the commission.
# You should chose a value for the hourly pay. The commission should be computed as a percentage of the weekly sales.
# You should choose a value for the percentage. Your program should output the pay based on the hours worked, the commission and the total pay for the week.
# Your program should include the pseudocode used for your design in the comments.
# Document the values you chose for the hourly rate and commission percentage in your comments as well.
# For the assignment simply write a short paragraph of any activities that you performed to show that your program works correctly.

#  program-set values - Hourly pay and commission (as a percentage)
hourly_pay = 15
commission = .20

# user input - get "number of hours worked for that week and the weekly sales."
weekly_hours = eval(input("How many hours did you work this week?: "))
weekly_sales = eval(input("How much was sold this week?: "))

# "compute the total pay as the sum of the pay based on the number of hours worked times the hourly rate plus the commission."
weekly_salary = hourly_pay * weekly_hours
weekly_commission = weekly_sales * commission
total_pay = weekly_commission + weekly_salary

#  "output the pay based on the hours worked, the commission and the total pay for the week"
print("Since you worked ", weekly_hours, "and your hourly rate is ", hourly_pay, " your weekly salary is ", weekly_salary)
print("And since you sold ", weekly_sales, "and your commission rate is ", commission, "you made ", weekly_commission, " in commission this week.")
print("Your weekly total pay is ", total_pay)