#program to find the area of triangle
import math
side1=int(input('enter side of nthe triangle :'))
side2=int(input('enter another side of a triangle :'))
side3=int(input('enter another side of a triangle :'))
s=(side1+side2+side3)/2
area=math.sqrt(s*(s-side1)*(s-side2)*(s-side34))
print('area of triangle is' ,area)


