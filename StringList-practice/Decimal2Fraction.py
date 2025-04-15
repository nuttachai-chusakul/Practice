import math
your_number = input('Enter your number : ').split(',')
denominator = int(('9'*len(your_number[2]))+('0'*len(your_number[1])))
numerator = (int(your_number[0])*denominator) + int(your_number[1]+your_number[2]) - int("0"+your_number[1])

gcd = math.gcd(numerator, denominator)

numerator //= gcd
denominator //= gcd

print(numerator, "/", denominator)