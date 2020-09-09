a=int(input('Enter year to check whether it is leap or not ')) 
if( (a%400==0 or a%4==0) and a%100!=0):
	print('Leap year') 
else:
	print('Not a leap year')