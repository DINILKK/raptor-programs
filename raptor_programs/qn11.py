#seconds into hours ,minutes and sec.
a=int(input("enter number of seconds :"))
hours=a//3600
minutes=(a%3600)//60
seconds=a%60
print(hours,"hours ",minutes,"minutes ",seconds,"seconds ")
