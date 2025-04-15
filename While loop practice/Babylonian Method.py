#This program is about finding the square root of a number by using Babylonian method

your_number = float(input("Enter your number : "))
guess = 1

if your_number < 0:
    print("Your number has no square root")

elif your_number == 0:
    guess = 0
    print("The square root of", your_number, "is", guess)

else:
    while abs(your_number - guess**2) > 10**(-8):
        guess = (guess + your_number/guess)/2
    print("The square root of", your_number, "is approximately", guess)
