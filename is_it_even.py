#Program to determine if a number is even or odd.

divisor = int(2)
dividend = int(input("What is your dividend?\n"))

even_or_odd = dividend % divisor

if even_or_odd == 0:
    print("Your dividend is an even number.")
else: print("Your dividend is an odd number.")
