input_string_var = input("Please enter a new password that contains at least 9 characters.") #Asks user to input password.

while len(input_string_var) <=8: # Checks to ensure password is proper length.
    input_string_var = input("Please try again, password must contain at least 9 characters.") # While not correct, informs user to try again.

print("Password successful.") # Once criteria is met, ends program and informs user.
