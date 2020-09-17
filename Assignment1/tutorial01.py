# Function to add two numbers 
def add(num1, num2): 
	addition = num1 + num2
	return addition

# Function to subtract two numbers 
def subtract(num1, num2): 
	subtraction = num1 - num2
	return subtraction

# Function to multiply two numbers 
def multiply(num1, num2): 
	#Multiplication Logic 
    multiplication=num1 * num2
    return multiplication

# Function to divide two numbers 
def divide(num1, num2): 
	#DivisionLogic
    if (num2==0):
	    return 0
    division = num1/num2
    if (isinstance(division,(float))):
	    return round(division,3)
    else:
	    return division

# Function to add power function
#You cant use the inbuilt python function x ** y . Write your own function
def power(num1, num2): #num1 ^ num2
	#DivisionLogic
	power=1
	if(isinstance(num1,(int, float)) and isinstance(num2,(int, float))):
		#go ahead
		if(num2<0):
			for i in range(abs(int(num2))):
				power=power*divide(1,num1)
		else:
			for i in range(abs(int(num2))):
				power=power*num1
	else:
		return 0
	if(isinstance(num1,(float))):
		return round(power,3)
	else:
		return power
	
# Python 3 program to print GP.  geometric Progression
#You cant use the inbuilt python function. Write your own function
def printGP(a, r, n): 
	gp=[]
	if (isinstance(a,(int, float)) and isinstance(n,(int))):
		for i in range(n):
			temp=multiply(a,power(r,i))
			gp.append(temp)
	return gp 

# Python 3 program to print AP.  arithmetic Progression
#You cant use the inbuilt python function. Write your own function
def printAP(a, d, n): 
	ap=[]
	if (isinstance(a,(int,float)) and isinstance(d,(int,float)) and isinstance(n,(int))):
		for i in range(n):
			term=a + multiply(i,d)
			ap.append(term)
	return ap

# Python 3 program to print HP.   Harmonic Progression
#You cant use the inbuilt python function. Write your own function
def printHP(a, d, n): 
	hp=[]
	if (isinstance(a,(int,float)) and isinstance(d,(int,float)) and isinstance(n,(int))):
		for i in range(n):
			aterm=divide(1,divide(1,a)+multiply(i,d))
			hp.append(aterm)
	return hp

