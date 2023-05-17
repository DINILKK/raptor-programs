#days into years,months
n=int(input("enter number of days :"))
years=n//365
months=(n%365)//30
days=(n%30)
print(years,"years ",months, " months",days," days" )