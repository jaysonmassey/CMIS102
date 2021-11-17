# Assignment 2 CMIS 102 Jayson Massey

# The second assignment involves writing a Python program to compute the price of a theater ticket.
# Your program should prompt the user for the patron's age and whether the movie is 3D.
# Children and seniors should receive a discounted price. x
# There should be a surcharge for movies that are 3D. x
# You should decide on the age cutoffs for children and seniors and the prices for the three different age groups. x
# You should also decide on the amount of the surcharge for 3D movies.
# Your program should output the ticket price for the movie ticket based on the age entered
# and whether the movie is in 3D.
# Your program should include the pseudocode used for your design in the comments.
# Document the values you chose for the age cutoffs for children and seniors,
# the prices for the three different age groups and the surcharge for 3D movies in your comments as well.

# Predefined variables
child_age = 12      # upper age limit
senior_age = 60     # lower age limit
child_discount = 5
senior_discount = 3
ticket_price = 15       # for ages 13 - 59
three_d_surcharge = 5

#  Get user input - "should prompt the user for the patron's age and whether the movie is 3D"
print("Welcome to Movie Calculator!  If you give me a little info, I'll tell you the price for your movie.")
patron_name = input("What is your name?")
print(patron_name, "what is your age?")
patron_age = eval(input())
print("Thanks", patron_name, "you're", patron_age, ".  Is the movie you want to see in 3D?  Yes or No?")
is_three_d = input()

# added logic to ensure that the user says yes or no to the 3D question
if is_three_d.lower() == "yes":     #used lower() here to allow answers like YES and Yes
    print("Your movie is in 3D")
    ticket_price = ticket_price + three_d_surcharge     # adds 3D surcharge
elif is_three_d.lower() == "no":
    print("Your movie is not in 3D")
else:
    print("I missed that", patron_name, ".  Is the movie you want to see in 3D?  Yes or No?")
    is_three_d = input()

#  logic for age-based discounts
if patron_age <= child_age:
    ticket_price = ticket_price - child_discount
    print("Child price")
elif patron_age >= senior_age:
    ticket_price = ticket_price - senior_discount
    print("Senior price")
else:
    print("Calculations done!")

# "output the ticket price for the movie ticket based on the age entered and whether the movie is in 3D."
print(patron_name, "I've calculated your movie price, and it's $",ticket_price,". Thanks for using Movie Calculator!")
