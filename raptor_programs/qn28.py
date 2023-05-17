#program to produce 1-4+9-16
n=int(input('enter number terms to be produced :'))
sum=0

for i in range(1,n+1):
  sq=i*i
  if sq%2==0:
    sum=sum-sq
  else:
    sum=sum+sq

print(sum)
