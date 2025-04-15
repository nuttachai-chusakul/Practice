number = input('Enter your number : ').strip()
step1 = number[3::7]
step2 = number[7::5]
step3 = str(int(step1) + int(step2) + 10000)
step4 = step3[-4:-1]
step5 = ((int(step4[-1])+int(step4[-2])+int(step4[-3]))%10)+1
step6 = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'[step5]
print(step4 + step6)







#92813912398100282033745980018127 --> 813C
#00000000000000000000000000000000 --> 000A
#99999999999999999999999999999999 --> 999H