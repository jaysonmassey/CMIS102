#   Final Project - CMIS 102 - Jayson Massey
#
#   The final project involves writing a Python program to determine the body-mass index
#   of a collection of six individuals. Your program should include a list of six names.
#   Using a for loop, it should successively prompt the user for the height in inches and weight
#   in pounds of each individual. Each prompt should include the name of the individual whose height and weight
#   is to be input. It should call a function that accepts the height and weight as parameters and
#   returns the body mass index for that individual using the formula weight × 703 / height2.
#   That body mass index should then be appended to an array. Using a second loop it should
#   traverse the array of body mass indices and call another function that accepts
#   the body mass index as a parameter and returns whether the individual is underweight, normal weight or overweight.
#   The number of individuals in each category should be counted and the number in each of those categories should
#   be displayed. You should decide on the names of the six individuals and the thresholds used for categorization.

#   ******     Variables    ******
bmi_names = ['Al', 'Bill', 'Cindy', 'Dee', 'Eli', 'Fred']           # hard-coded names
first_loop = 0                              # for 1st for loop
second_loop = 0                             # for 2nd for loop
number_of_bmi = [0, 1, 2, 3, 4, 5]          # constant that controls the number of times the loop happens (6)
bmi_height = 0                              # height
bmi_weight = 0                              # weight
bmi_formula = 0                             # weight * 703 / height^2.
bmi_list = []                               # empty list to remember bmi
append_bmi = 0
under_weight_bmi = 0
normal_weight_bmi = 0
over_weight_bmi = 0
obesity_bmi = 0
put_bmi = 0                                 # Here as global variable for categorize function
count_under_weight_bmi = 0                  # These used to display and remember bmi categories at the end.
count_normal_weight_bmi = 0                 #   BMI Categories:
count_over_weight_bmi = 0                   #       Underweight = <18.5         Normal weight = 18.5–24.9
count_obesity_bmi = 0                       #       Overweight = 25–29.9        Obesity = BMI of 30 or greater

#   ******  Functions   *******
#   calc_bmi
#       takes height and weight and returns the BMI using weight * 703 / height^2 formula
def calc_bmi(calc_height,calc_weight):
    calc_my_bmi = calc_weight * (703 / (calc_height * calc_height))
    print("The BMI for this person:", calc_my_bmi)
    return calc_my_bmi
# 	categorize_bmi
# 	    Accepts the BMI as a parameter and returns whether the BMI is categorized as:
#       Underweight = <18.5, Normal weight = 18.5–24.9, Overweight = 25–29.9 or Obesity = BMI of 30 or greater
def categorize_bmi(put_bmi):
    put_underw = 0
    put_normalw = 0
    put_overw = 0
    put_obesity = 0
    if put_bmi < 18.5:
        # print("Found under weight in function categorize_bmi", put_bmi)
        put_underw = put_underw + 1
    elif put_bmi >= 18.5 and put_bmi <= 24.9:
        # print("Found normal weight in function categorize_bmi", put_bmi)
        put_normalw = put_normalw + 1
    elif put_bmi >= 25 and put_bmi <= 29.9:
        # print("Found over weight in function categorize_bmi", put_bmi)
        put_overw = put_overw + 1
    else:
        # print("Found obesity in function categorize_bmi", put_bmi)
        put_obesity = put_obesity + 1
    return put_underw,put_normalw,put_overw,put_obesity         # Return the BWI categories

#   *****   Main Program    ******
print("Enter each of six people's height and weight!  Get back the BMI of each person.\n")

for first_loop in number_of_bmi:
    print("Enter the bmi height in inches for", bmi_names[first_loop])
    bmi_height = int(input())
    print("Enter the bmi weight:")
    bmi_weight = int(input())
    append_bmi = calc_bmi(bmi_height, bmi_weight)           # Call function to get the BMI for this person
    bmi_list.append(append_bmi)                             # Append bmi to an array

print("First loop bmi", bmi_list)                           # Show the entire BMI array

# 	Traverse the BMI array - call another function that accepts the BMI as a parameter and returns the BMI category
#   The BMI in each category should be counted and the number in each of those categories should be displayed.
for second_loop in number_of_bmi:
    under_weight_bmi,normal_weight_bmi,over_weight_bmi,obesity_bmi = categorize_bmi(bmi_list[second_loop])
    if under_weight_bmi == 1:
        count_under_weight_bmi = count_under_weight_bmi + 1
    elif normal_weight_bmi == 1:
        count_normal_weight_bmi = count_normal_weight_bmi + 1
    elif over_weight_bmi == 1:
        count_over_weight_bmi = count_over_weight_bmi + 1
    else:
        count_obesity_bmi = count_obesity_bmi + 1

#   print category results
print("The number of under weight BMI is:", count_under_weight_bmi)
print("The number of normal weight BMI is:", count_normal_weight_bmi)
print("The number of over weight BMI is:", count_over_weight_bmi)
print("The number of obesity BMI is:", count_obesity_bmi)