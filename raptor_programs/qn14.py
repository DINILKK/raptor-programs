#whether a number is palindrome
num1=int(input("enter a number :"))
pal=num1
num2=0
while num1>0:
  num2=num2*10+(num1%10)
  num1=num1//10

if num2==pal:
  print("the given number is a palindrome")
else:
  print("the given number is not a palindrome")
  