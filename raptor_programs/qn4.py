
#sum of the factors of a number
number=int(input("enter a number :"))
sum=0
for i in range(1,number):
  if number%i==0:
    sum=sum+i

print(sum)
