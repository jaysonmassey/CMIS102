#   Assigment Six - CMIS 102 - Jayson Massey
#   The sixth assignment involves writing a Python program to read in the temperatures,
#   as user input, for ten consecutive days in Celsius and store them into an array.
#   The entire array should then be displayed.
#   Next each temperature in the array should be converted to Fahrenheit
#   and the entire array should be again be displayed.
#   The formula for converting Celsius to Fahrenheit is °F = (°C × 1.8) + 32.
#   Finally, the number of cool, warm and hot days should be counted and the number
#   of each type of days should be displayed.
#   You should decide on the thresholds for determining whether a day is cool, warm or hot..
#   Logic:
#   -   Create a loop that gets ten temperatures
#   -   Convert Celsius to Fahrenheit
#    -   Determine if temp is hot, warm or cool
#    -   Display temp
#
#   Variables
day_limit = 10       # easier to change for testing
temperatures = []
hot_limit = 80
warm_limit = 60

celsius_count = 1
#   get number of elements in array temperatures[]
while celsius_count <= day_limit:
    print("This program calculates temperatures from Celsius to Fahrenheit for ten day")
    print("Enter the temperature in Celsius for Day", celsius_count)
    add_temp = int(input())
    temperatures.append(add_temp)
    celsius_count = celsius_count + 1

print(temperatures)                               # check for ten temps

array_count = 0                                     # This is just for updating the temp from C to F
f_count = 1                                         # Doing this to avoid showing day 0
f_temp = 0
new_temp = 0
while f_count <= day_limit:
    f_temp = temperatures[array_count]              #   get the temp from the array
    new_temp = (f_temp * 1.8) + 32                  #   calculate the Celsius temp into Fahrenheit
    temperatures[array_count] = new_temp            #   convert the element in the array from C to F
    print("The temperature in Celsius for Day", f_count, "is", f_temp)
    print("The temperature in Fahrenheit for Day", f_count, "is", temperatures[array_count])
    if new_temp >= hot_limit:                       #   logic for hot, warm or cool temps
        print("The temperature is HOT\n")
    elif new_temp >= warm_limit and new_temp < hot_limit:
        print("The temperature is warm\n")
    else:
        print("The temperature is cool\n")
    f_count = f_count + 1
    array_count = array_count + 1

print(temperatures)                                 # check for ten new temps