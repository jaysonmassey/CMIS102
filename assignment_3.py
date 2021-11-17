#Assignement 3 - CMIS 102 - Jayson Massey

# The third assignment involves writing a Python program to compute the cost of carpeting a room.
# Your program should prompt the user for the width and length in feet of the room and the quality of carpet to be used.
# A choice between three grades of carpeting should be given.
# You should decide on the price per square foot of the three grades on carpet.
# Your program must include a function that accepts the length, width, and carpet quality as parameters and
# returns the cost of carpeting that room. After calling that function,
# your program should then output the carpeting cost.

# constants are carpet prices
silver_price = 3
gold_price = 6
platinum_price = 10

# functions
def capture_quality(get_quality): # logic to ensure that user enters the number 0, 1, or 2
    if get_quality == 1:
        print(get_quality)
    elif get_quality == 2:
        print(get_quality)
    elif get_quality > 2:        # test cases for when the quality grade >= 3
        print("Enter the carpet quality.  Choose 0 for silver, 1 for gold, and 2 for platinum:")
        get_quality = eval(input())
        print(get_quality)
    else:                         # this test case catches all other numerical cases
        get_quality = 0
        print(get_quality)

# logic to calculate price (w * d) * carpet quality price and returns the total price
def calc_price(cust_width, cust_length, cust_quality):
    if cust_quality == 0:
        total_price = ((cust_width * cust_length) * silver_price)
        print("The total price is", total_price)
    elif cust_quality == 1:
        total_price = ((cust_width * cust_length) * gold_price)
        print("The total price is", total_price)
    else:
        total_price = ((cust_width * cust_length) * platinum_price)
        print("The total price is", total_price)

# get user inputs: length, width, and carpet quality
print("Enter the room width in feet:")
room_width = eval(input())
print("Enter the room length in feet:")
room_length = eval(input())
print("Enter the carpet quality.  Choose 0 for silver, 1 for gold, and 2 for platinum:")
carpet_quality = eval(input())
capture_quality(carpet_quality)  # the logic gets the user to enter a number
calc_price(room_width, room_length, carpet_quality)  # price gets calcuated here
