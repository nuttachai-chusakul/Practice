#This program checks if the inputted number is an increasing digit number.
your_number = int(input(">> "))
is_increasing = True
right_digit = 99
while your_number > 0:
    left_digit = your_number % 10
    your_number //= 10
    if left_digit >= right_digit:
        is_increasing = False
        break
    right_digit = left_digit

if is_increasing:
    print("Yes, this is an increasing-digit number")
else:
    print("No, this is not an increasing-digit number")