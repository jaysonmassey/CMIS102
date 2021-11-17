#   Final Project - CMIS 102 - Jayson Massey
#   The practice final project involves writing a Python program to determine the
#   densities of a collection of cylindrical containers .
#   Your program should include a list of the contents of the five containers.
#   Using a for loop, it should successively prompt the user for the height and diameter in feet and
#   weight in pounds of each container.
#   Each prompt should include the contents of the container whose dimensions and weight is to be input.
#   It should call a function that accepts the height, diameter and weight as parameters and
#   returns the density for that container. The volume of a cylinder is calculated as diameter × π × height.
#   Density is calculated as weight / volume. The density should be appended to an array.
#   The complete array should then be displayed.
#   Using a second loop it should traverse the array of densities and call another function that accepts
#   the density as a parameter and returns whether the container has low density, average density or high density.
#   The number of containers in each category should be counted and
#   the number in each of those categories should be displayed.
#   You should decide on the contents of the five containers and the thresholds used for categorization.

import math                             # for pi (a constant).  Use math.pi
# Variables
first_loop = 0                          # for 1st for loop
second_loop = 0                         # for 2nd for loop
number_of_containers = [0, 1, 2, 3, 4]  # constant that controls the number of times the loop happens
container_height = 0                    # height
container_diameter = 0                  # diameter
container_weight = 0                    # weight
container_volume = 0                    # volume = diameter × π × height
container_density =  0                  # Density = weight / volume
density_list = []                       # empty list to remember density
number_low_density = 0
number_medium_density = 0
number_high_density = 0
count_low_density = 0                  # these last three are used to display density categories at the end.
count_medium_density = 0               # -  Low density > 1
count_high_density = 0                 # -  Medium density between 1 and 3
                                       # -  High desity > 3
#   Functions:
#   -   calc_volume - takes height and diameter and weight and returns the volume and density
def calc_volume(num_height, num_diameter, num_weight):      # expects three arguments
    print(num_height, num_diameter, num_weight)
    num_volume = num_diameter * math.pi * num_height        # volume = diameter × π × height
    print("Volume:", num_volume)
    num_density = num_weight / num_volume                   # Density = weight / volume
    print("Density:", num_density)
    return num_volume, num_density                          # Return the volume then the density

# 	get density category
# 	-   accepts the density as a parameter and returns whether the container
# 	    has low density, average density or high density
def determine_density(put_density):
    put_low_density = 0
    put_medium_density = 0
    put_high_density = 0
    if put_density < 1:
#        print("Found low density in function", put_low_density)
        put_low_density = put_low_density + 1
    elif put_density >= 1 and put_density <= 3:
#        print("Found mid density in function", put_medium_density)
        put_medium_density = put_medium_density + 1
    else:
#        print("Found high density in function", put_high_density)
        put_high_density = put_high_density + 1
    print("Exit if logic: Low", put_low_density, "Avg", put_medium_density, "High", put_high_density)
    return put_low_density,put_medium_density,put_high_density            # Return the low, avg, and high densities

#   Main Program
print("Enter the container height, diameter and weight and get back the volume and density of the container.\n")
# 	5 times:
# 	-	print prompt for height and diameter and weight
# 	-	get height and diameter and weight
# 	-	call function  that takes height and diameter and weight and returns the volume and density
# 	-	return density to an array
# 		-	The volume of a cylinder is calculated as diameter × π × height.
# 		-	Density is calculated as weight / volume
for first_loop in number_of_containers:
    print("Enter the container height:")
    container_height = int(input())
    print("Enter the container diameter:")
    container_diameter = int(input())
    print("Enter the container weight:")
    container_weight = int(input())
    print("Container height:", container_height)                        # Display user input
    print("Container diameter:", container_diameter)
    print("Container weight:", container_weight)
    container_volume,container_density = calc_volume(container_height, container_diameter, container_weight)
    density_list.append(container_density)                              # Append density to an array.
    print("First loop container volume:", container_volume)
    print("First loop container density:", container_density)

print("Print all of the densities:", density_list)                         # Show complete array

#   Display density categories
# 	-	traverse the array of densities
# 	-	Call another function that accepts the density as a parameter and returns whether the container
# 		has low density, average density or high density
#   -   The number of containers in each category should be counted and
#       the number in each of those categories should be displayed.
for second_loop in number_of_containers:
    number_low_density,number_medium_density,number_high_density = determine_density(density_list[second_loop])
    if number_low_density == 1:
        count_low_density = count_low_density + 1
    elif number_medium_density == 1:
        count_medium_density = count_medium_density + 1
    else:
        count_high_density = count_high_density + 1
#   print category results
print("The number of low density containers is:", count_low_density)
print("The number of average density containers is:", count_medium_density)
print("The number of high density containers is:", count_high_density)
print("The full density list after the second loop is:", density_list)