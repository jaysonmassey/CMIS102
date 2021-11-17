# Week 4 Discussion - CMIS 102 - Jayson Massey

# Write a program to calculate the cost of a visit to a gasoline station.
# Your program should prompt the user for the grade of gasoline, either regular, mid-grade, or premium,
# the number of gallons, and whether a car wash is desired. Your program must include
# a function that accepts the number of gallons, and grade of gasoline as parameters
# and returns the cost of the gasoline. The program should then display the cost of the visit
# including the car wash if one was included.
# Your program should include the pseudocode used for your design in the comments.
# Document the values you chose for the price of the car wash and three grades on gasoline in your comments as well.

import math
cost_of_gallons = 4  # in dollars
cost_of_car_wash = 10 # in dollars
midgrade_surcharge = 1
premium_surcharge = 2
gasoline_grade = ("regular", "mid-grade", "premium")  # a tuple that contains the list of gasoline grades
# "prompt the user for the grade of gasoline, either regular, mid-grade, or premium,
# the number of gallons, and whether a car wash is desired."
print("Choose 0 for regular, 1 for mid-grade, 2 for premium: ")       # Get user input for gas grade
user_grade = eval(input())
print(user_grade) # **** for debugging ****
if user_grade == 1:
    cost_of_gallons = cost_of_gallons + midgrade_surcharge
elif user_grade == 2:
    cost_of_gallons = cost_of_gallons + premium_surcharge
elif user_grade > 2:        # test cases for when the gasoline grade >= 3
    print("Please choose 0 for regular, 1 for mid-grade, 2 for premium: ")
    user_grade = eval(input())
else:                         # this test case catches all other cases and makes the gasoline grade regular
    user_grade = 0

print(gasoline_grade[user_grade])
print("Enter number of gallons desired: ")  # get user input for number of gas gallons
number_of_gallons = eval(input())
print("You need", number_of_gallons, "gallons of gas")
total_price = number_of_gallons * cost_of_gallons  #  calculate total price before car wash

print("Would you like a car wash?  Enter 1 for Yes or 0 for No")
is_Car_Wash = eval(input())  # Going to use Boolean for this, so 0 is false and all other numbers are true
if is_Car_Wash == 0:
    print("No car wash for you today")
else:
    print("Thanks for getting a car wash!")
    total_price = total_price + cost_of_car_wash  # add car wash to total price

print("Your total price today is", total_price)  # display total price
root_price = math.sqrt(total_price)     # get square root of the price
print("The square root of your total price is", root_price)  # computation w/ predefined functions in math library


