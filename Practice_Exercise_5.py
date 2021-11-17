#  The fifth practice assignment involves writing a Python program to determine whether a string
#  is in the correct format for a university e-mail address. Your program should prompt the user for
#  the candidate e-mail address and output either that the address is valid or the reason it is invalid.
#  It must end with the substring .edu. Finally, it must contain the @ symbol is some position
#  other than the first or last character. To be valid the length of the user name
#  before the @ symbol must greater than some minimum length.
#  You should decide on the minimum allowable length.  <-- 7 characters

#  Minimum allowable length.  <-- 7 characters
min_e_mail = 7
#  Int to create valid email logic checkpoints
valid_e_mail = 0

# Your program should include the pseudocode used for your design in the comments.
# Document the values you chose for the minimum  allowable length in your comments as well.

# Input - get email from user
print("Enter an email address, and I will tell you if it is valid or invalid")
e_mail = input()

# Check the minimum email length
length = len(e_mail)
if length >= min_e_mail:
    print("The email address is", length, "characters, which is past the minimum length of", min_e_mail)
    valid_e_mail = valid_e_mail + 1
    print(valid_e_mail)
elif length < min_e_mail:
    print("The email address is", length, "characters.  This does not meet the minimum length of", min_e_mail)
    print(valid_e_mail)
else:
    exit()

#  Verify that there is a .edu
find_edu = e_mail.find('.edu')
if find_edu >= 1:
    print(".edu domain found")
    valid_e_mail = valid_e_mail + 1
    print(valid_e_mail, e_mail[-4:])
elif find_edu <= 0:
    print(".edu domain not found")
    print(valid_e_mail, e_mail[-4:])  # slice!
else:
    exit()

#  Verify that the email contains the @ symbol other than first and last character
find_at_sign = e_mail
first_sign = find_at_sign[0]
last_sign = find_at_sign[length - 1]
if (first_sign or last_sign)  == "@":
    print("Found an invalid character")
    print(first_sign)
    print(last_sign)
    print(valid_e_mail)
elif (first_sign or last_sign)  != "@":
    valid_e_mail = valid_e_mail + 1
    print(valid_e_mail)
else:
    exit()

#  Show that the email is valid because it passed all 3 checks
if valid_e_mail == 3:
    print("This email is valid")
    print(valid_e_mail)
elif valid_e_mail != 3:
    print("This email is not valid")
    print(valid_e_mail)
else:
    exit()