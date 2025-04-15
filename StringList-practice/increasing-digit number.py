#This program checks if a number is an increasing-digit number
your_number = input("Enter digits : ").strip()
is_increasing = True
left_digit = ""
for e in your_number:
    if e <= left_digit:
        is_increasing = False
        break
    left_digit = e
if is_increasing:
    print("Yes, this is an increasing-digit number")
else:
    print("No, this is not an increasing-digit number")