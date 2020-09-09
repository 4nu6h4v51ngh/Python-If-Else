print('Largest among Three nos.')
a=int(input('Enter first no. '))
b=int(input('Enter second no. '))
c=int(input('Enter third no. '))
if(a>b and a>c):
	print('%d is greatest'%(a))
elif(b>c):
	print('%d is greatest'%(b))
else:
	print('%d is greatest'%(c))	