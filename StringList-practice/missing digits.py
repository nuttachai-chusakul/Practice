#This program finds missing digits in a given number
your_number = input("Enter digits : ").strip()
check = [False]*10
number_of_missing = 0
missing_number = ""
for d in your_number:
    check[int(d)] = True


for i in range(len(check)):
    if check[i] == False:
        missing_number += " " + str(i)
        number_of_missing += 1

if number_of_missing > 1:
    print("The missing digits are" + missing_number)

elif number_of_missing == 1:
    print("The only missing digit is" + missing_number)

else:
    print("There is no missing digits")