#program to calculate the distace between two points
p1=int(input('plot a point'))
p2=int(input('plot another point'))

distance=p2-p1

if distance<0:
  distance=-1*distance
  print(distance)

else:
  print(distance)

