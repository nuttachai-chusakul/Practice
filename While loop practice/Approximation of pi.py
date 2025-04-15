#This program finds a fraction that approximates pi more accurately than 22/7.
import math
numerator = 22
denominator = 7
pi = math.pi

while abs(pi - (numerator/denominator)) > 1e-10:
    delN = abs(pi - (numerator+1)/denominator)
    delD = abs(pi - numerator/(denominator+1))
    
    if delN < delD:
        numerator += 1
    else:
        denominator += 1

print("The approximation of pi is "+ str(numerator)+"/"+str(denominator))
