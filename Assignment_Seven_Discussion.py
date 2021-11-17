#   Week Seven Discussion - CMIS 102 - Jayson Massey
#   Post a Python program that contains an array variable whose values are input by the user.
#   It should the perform some modification to each element of array using a loop
#   and then the modified array should be displayed.
#   Variables
number_of_people = 0    # gets number of people to weigh
weight_pounds = []      # empty array for weights

#   get number of elements in array
print("This program calculates weights from pounds to stone")
print("Enter the number of people who need their weight in stone")
number_of_people = int(input())

#   Fill the array with values in pounds
array_number = 0
array_input = ''
count = 1
while count <= number_of_people:
    print("Enter the weight of person number", count, "in pounds")
    array_input = int(input())
    weight_pounds.append(array_input)         #    used append to assign a value to an index that doesn't exist.
    count = count + 1
    array_number = array_number + 1

for_loop = 0
weight_stone = []
add_stone = ''
#   Print the array
for for_loop in range(len(weight_pounds)):      # used this to "produce a loop over a sequence of integers"
    print("The weight of person number", for_loop, "is", weight_pounds[for_loop], "pounds")
    add_stone = weight_pounds[for_loop] * 0.0714286             # convert weight in pounds to stone
    weight_stone.append(add_stone)
    print("The weight of person number", for_loop, "is", weight_stone[for_loop], "in stone")  # display weight in stone