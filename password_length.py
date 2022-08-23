password = input("Please enter a new password that contains at least 9 characters.") #Asks user to input password.
if len(password) <=8: #checks to ensure password is proper length.
    input("Please try again, password must contain at least 9 characters.") #if not correct, informs user to try again.
elif len(password) >=8: #checks to ensure password is proper length.
    print("Password successful.") #if correct, tells user it is correct.

#need to learn how to add proper loop functionality until password meets criteria. 
