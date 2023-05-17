#program to check if the given number is armstrong or not.
num1=int(input('enter a number :'))
count=0
num2=0
num3=num1

while num1>0:
  num1=num1//10
  count=count+1

num1=num3

while num1>0:
  r=(num1%10)
  num2=num2+r**count
  num1=(num1//10)

num1=num3

if num2==num1:
  print("its an armstrong number !!!")

else:
  print('its not')

  
