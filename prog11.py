print('Enter values to find roots are real,imaginary')
a=int(input("The value of a "))
b=int(input("The value of b "))
c=int(input("The value of c "))
d=b*b-4*a*c
if (d==0):
  print("Both roots are equal")
  x1=-b/(2.0*a);
  x2=x1;
  print("First  Root Root1= %f"%x1)
  print("Second Root Root2= %f"%x2)
elif d>0:
	int("Both roots are real and diff")
	x1=(-b+sqrt(d))/(2*a)
	x2=(-b-sqrt(d))/(2*a)
	print("First  Root Root1= %f"%x1)
	print("Second Root root2= %f"%x2)
else:
  print("roots are imaginary")