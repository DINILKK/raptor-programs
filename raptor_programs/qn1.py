#program to find the smallest digit in a two digit number
number=int(input("enter a two digit number :"))
l=number%10
f=number//10
if l<f:
  print(l)
elif f<l:
  print(f)

