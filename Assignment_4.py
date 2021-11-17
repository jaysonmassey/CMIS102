#  Assignment 4 - CMIS 102 - Jayson Massey
#  Directions: Compute the average quiz grade for a group of five students.
#  Your program should include a list of five names.
#  Using a for loop, it should successively prompt the user for the quiz grade for each of the five students.
#  Each prompt should include the name of the student whose quiz grade is to be input.
#  It should compute and display the average of those five grades and the highest grade.
#  You should decide on the names of the five students.

# Python function to get average of a list
def myAverage(my_list):
    return sum(my_list) / len(my_list)

# Python function to get the highest score
def highest_score(class_score):
    high_grade = None
    # print("Before:", high_grade)
    for itervar in class_score:
        if high_grade is None or itervar > high_grade:
            high_grade = itervar
        # print("Current value:", itervar, " Largest so far", )
    print("Highest quiz score is:", high_grade)

# define variables
student_names = ['Mark', 'Amber', 'Todd', 'Anita', 'Sandy']
student_scores = []     # empty list to fill with user-entered quiz grades
list_size = 5

#  Get quiz score for each student
print("\n")
i = 0
while i < 5:
    print("Enter the quiz score for", student_names[i], ":")
    item = int(input())
    student_scores.append(item)
    print("The student score is", item)
    i = i + 1

#  Run function for average score
average = myAverage(student_scores)
# Printing average quiz score
print("\n")  # print a new line for spacing
print("Average quiz score is", round(average, 2))
# run function for highest quiz score
highest_score(student_scores)

