# Week 3 Example 2 CMIS 102 Jayson Massey
# Objective: Write a program that asks the user to enter three numbers
# and determines the largest value of the three
# and displays that largest value.
# Here is the pseudocode:
#     read in three numbers
#     if the first is larger than other two, it is largest
#     else if the second it is larger than other two, it is largest
#     if neither of those were true, the third number must be largest

print("The program will determine which number is the largest.")
print("Enter the first number: ")
num1 = eval(input())
print("Enter the second number: ")
num2 = eval(input())
print("Enter the third number: ")
num3 = eval(input())

if (num1 > num2) and (num1 > num3):
    print("The first number ", num1, " is the largest number. The other values are ", num2, " and ", num3)
elif (num2 > num1) and (num2 > num3):
    print("The second number ", num2, " is the largest number. The other values are ", num1, " and ", num3)
elif (num3 > num1) and (num3 > num2):
    print("The third number ", num3, " is the largest number.  The other values are ", num1, " and ", num2)
else:
    print("The numbers are the same! ", num1, num2, num3)