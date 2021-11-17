# Assignment Five - CMIS 102 - Jayson Massey
# The fifth assignment involves writing a Python program to determine whether a password meets all the requirements
# for a secure password. Your program should prompt the user for the candidate password and output either that
# the password is valid or the reason it is invalid. To be valid the length of the password must greater than
# some minimum length but less than some maximum.
# It must not include the substring "umgc" in any combination of upper or lower case letters.
# Finally, it must contain the # symbol in some position other than the first or last character.
# You should decide on the minimum and maximum allowable lengths.
#
# Your program should include the pseudocode used for your design in the comments.
# Document the values you chose for the minimum and maximum allowable lengths in your comments as well.
#
# You are to submit your Python program as a text file (.py) file. In addition, you are also to submit a test plan
# in a Word document or a .pdf file. 15% of your grade will be based on whether the comments in your program include
# the pseudocode and define the values of your constants, 70% on whether your program executes correctly
# on all test cases and 15% on the completeness of your test report.

# Variables - Added to meet requirement of project
bad_string = "umgc"
required_symbol = "#"
min_length = 8
max_length = 16
my_password = None
valid_password_flag = 0

def get_password():
# Input - get password from user and initialize variables
    print("Enter a password, and I will tell you if it is valid or invalid.")
    print("A valid password is between 8 and 16 characters.  It contains a # that is not the first or last character.")
    print("A valid password also does not contain 'umgc' in any combination of upper or lower case letters")
    my_password = input()
    password_length = len(my_password)

# Check password contents
print("First character:", my_password[:1])
print("Last character:", my_password[-1:])
print("Other characters:", my_password[1:-1])

# Check for the length
if (password_length >= min_length) and (password_length <= max_length):
    print("The password is", password_length, "characters, which is between", min_length, "and", max_length)
    valid_password_flag = valid_password_flag+ 1
    print("Flag counter:", valid_password_flag)  # Checking password flag
else:
    print("This password is invalid. Disallowed string length.")
    exit()

# Check if first or last character is a hastag
if (required_symbol in my_password[1:-1]) == False:
    print("This password is invalid.  Hashtag (#) is required in password.")
    exit()
elif (required_symbol in my_password[1:-1]) == True:  # see if hashtag is in a character that is not first or last
    valid_password_flag = valid_password_flag + 1
    print("The rest of the password", my_password[1:-1])
    print("Flag counter:", valid_password_flag)  # Checking password flag
else:
    print("This password is invalid.  Illegal character.")
    exit()

# Check substring "umgc" in any combination of upper or lower case letters
lower_password = my_password.lower()  # Convert the password to lower-case to eliminate all upper-case test cases
print(lower_password.find(bad_string))
if lower_password.find(bad_string) == -1:  # Is umgc in the password?
    print("Password in lower case:", lower_password)
    print("The invalid string:", bad_string)
    valid_password_flag = valid_password_flag + 1
    print("Flag counter:", valid_password_flag)  # Checking password flag
else:
    print("This password is invalid.  Illegal character string in password")
    print("Password in lower case:", lower_password)
    print("The invalid string:", bad_string)
    exit()



