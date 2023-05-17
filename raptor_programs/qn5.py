#program to find largest among three numbers
a=int(input("enter a number :"))
b=int(input("enter another number :"))
c=int(input("enter another number :"))
if a>b and a>c:
  print(a,"is the largest")
elif b>a and b>c:
  print(b,"is the largest")
else:
  print(c,'is the largest')


