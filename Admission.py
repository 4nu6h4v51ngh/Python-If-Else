p=int(input("Input the marks obtained in Physics :"))

c=int(input("Input the marks obtained in Chemistry :"))

m=int(input("Input the marks obtained in Mathematics :"))

print("Total marks of Maths, Physics and Chemistry : %d" %(m+p+c))
print("Total marks of Maths and  Physics : %d " %(m+p))
if (((m>=65) and (p>=55)) and (c>=50)) and ((m+p+c)>=180 or (m+p)>=140):
	print("The  candidate is eligible for admission")
else:
    print("The candidate is not eligible")
