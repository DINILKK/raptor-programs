#program to the HCF of two number
num1=int(input('enter a number :'))
num2=int(input('enter another number :'))

if num1<num2:
  for i in range(1,(num2//2)+1):
    if num1%i==0 and num2%i==0:
      hcf=i

else:
   for i in range(1,(num1//2)+1):
    if num1%i==0 and num2%i==0:
      hcf=i


print(hcf)


