#reverse of a number
num1=int(input('enter a number :'))
rev_num1=0

while num1>0:
  rev_num1=rev_num1*10+(num1%10)
  num1=num1//10

print('there reverse of the given number',rev_num1)
