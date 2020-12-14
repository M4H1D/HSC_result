print("Your HSC result will be announced by SSC gpa 75% and JSC gpa 25% .")
x=float(input("Enter your SSC gpa= "))
if (x==5.00):
	print("SSC=A+")
elif (4.00<=x<=4.99):
	print("SSC=A")
elif(3.00<=x<=3.99):
	print("SSC=A-")
elif(2.00<=x<=2.99):
	print("SSC=B")
elif(1.00<=x<=1.99):
	print("SSC=D")
elif(0.0<=x<=0.99):
	print("SSC=F")
else:
	print("error")
	
y=float(input("Enter your JSC gpa= "))
if (y==5.00):
	print("JSC=A+")
elif (4.00<=y<=4.99):
	print("JSC=A")
elif(3.00<=y<=3.99):
	print("JSC=A-")
elif(2.00<=y<=2.99):
	print("JSC=B")
elif(1.00<=y<=1.99):
	print("JSC=D")
elif(0.0<=y<=0.99):
	print("JSC=F")
else:
	print("error")

#ekhon hsc gpa bair korbo
a=((x*75)/100)
b=((y*25)/100)
c=(a+b)
if (0.0<=a<=3.75) and (0.0<=b<=1.25):
	if (0<=c<=5):
		print("your HSC result=",c)
		if (c==5.00):
			print("HSC=A+")
		elif (4.00<=c<=4.99):
			print("HSC=A")
		elif(3.00<=c<=3.99):
			print("HSC=A-")
		elif(2.00<=c<=2.99):
			print("HSC=B")
		elif(1.00<=c<=1.99):
			print("HSC=D")
		elif(0.0<=c<=0.99):
			print("HSC=F")
	else:
		print("faijlami korle HSC result show korbe na")
else:
	print("faijlami koris na.faijlami korle tor result show korbe na")
if c==5.00:
	print("Congratulation,You have got A+.")
