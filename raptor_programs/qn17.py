#program to check if a number is automophic
num1=int(input('enter a number :'))
i=0
num2=num1
sq=num2*2

while num2>0:
  num2=num2//10
  i=i+1
  
