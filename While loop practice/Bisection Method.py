#This program is about finding the square root of a number by using Bisection method

your_number = float(input("Enter your number : "))
if your_number < 0:
    print("Your number has no square root")

elif your_number == 0:
    print("The square root of", your_number, "is 0.0")

else:
    lower = 0
    upper = max(1.0, your_number)
    answer = (lower+upper)/2

    while abs(answer**2 - your_number) > 1e-5:
        answer = (lower+upper)/2
        if answer**2 > your_number:
            upper = answer
        else:
            lower = answer

    print("The square root of", your_number, "is approximately", answer)