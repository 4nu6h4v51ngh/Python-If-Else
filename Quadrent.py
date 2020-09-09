print("Enter the values to determine in which quadrant the coordinate point lies ")
a=int(input('Enter 1st coordinate '))
b=int(input('Enter 2nd coordinate '))
if( a > 0 and b > 0):
	print("The coordinate point (%d,%d) lies in the First quandrant" %(a,b))
elif( a < 0 and b > 0):
	print("The coordinate point (%d,%d) lies in the Second quandrant" %(a,b))
elif( a < 0 and b < 0):
	print("The coordinate point (%d, %d) lies in the Third quandrant" %(a,b))
elif( a > 0 and b < 0):
	print("The coordinate point (%d,%d) lies in the Fourth quandrant" %(a,b))
else:
	print("The coordinate point (%d,%d) lies at the origin" %(a,b))
