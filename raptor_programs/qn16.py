#To convert binary to  decimal
num1=int(input('enter a binary number :'))
num2=0
i=1

while num1!=0:
  rem=num1%10
  num2=num2+(rem*i)
  i=i*2
  num1=num1//10

print("the decimal value for the given number is :",num2)
