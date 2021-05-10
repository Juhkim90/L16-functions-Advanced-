'''
# Lesson 1

# get Name function 
def getName(): 
	userName = input("Please tell me your name: ")
	# userName variable is specific to this function
	return userName 

def greetUser(name): # parameter variables are specific to the function 
	print("Hi " + name)
 
greetUser(getName())
greetUser(getName())
greetUser(getName())

# ask the user for two numbers 
#num1 = int(input("Please give me a number: "))
#num2 = int(input("Please give me a second number: "))

# write a function that takes num1 and num2 as parameters
# prints the sum 
def sum(numList): 
	total = 0 
	for index in numList: 
		total += index 
	print("The sum is " + str(total))

sum([1,2,3,4,5,6,7,8,9,10]) # 55

# function for product 
def product(numList): 
	total = 1 
	for index in numList: 
		total *= index 
	print("The product is " + str(total))

product([1,2,3,4,5,6,7,8,9,10])
'''




#Lesson 2

numbers = []

def getNumbers():
	userNumber = inpout("Enter a number or 'q' to quit: ")
	while(userNumber != 'q'):
		numbers.append(int(userNumber))
		userNumber = inpout("Enter a number or 'q' to quit: ")

getNumbers()

def sum(numberList):
	total = 0
	for index in numberList:
		total += index

	print("The sum is " + str(total))

sum(numbers)

def product(numberList):
	total = 1
	for index in numberList:
		total *= index

	print("The product is " + str(total))

product(numbers)





'''
Warm Up2 - Fahrenheit to Celsius conversion
Given: (F − 32) × 5/9 = C

def tempConvert (?):


temp = ?
print (?)
>> # F = # C

'''

# Warm Up2 - Fahrenheit to Celsius conversion
# Given: (F − 32) × 5/9 = C
def tempConvert(t):
	return (t - 32) * 5 / 9

temp = float(input("Temperature in Fahrenheit: "))
print(str(temp) + " F = " + str(tempConvert(temp)) + " C")



def getInfo(name, age, school):
	print("Name: " + name)
	print("Age: " + age)
	print("School: " + school)

getInfo(input("What is your name? "),input("How old are you? "),input("What is your school name? "))



# New Notes
def factorial(x):
	if (x == 1):
		return 1
	else:
		return x * factorial(x - 1)

num = int(input("Factorial number: "))
print ("The factorial of " + str(num) + " is " + str(factorial(num)))



'''
Codingbat
Practice Question

The parameter weekday is True if it is a weekday,
and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation.
Return True if we sleep in.
'''

def sleep_in(weekday, vacation):
	return (not weekday or vacation)

# Test runs
print (sleep_in(False, False)) # True
print (sleep_in(True, False)) # False
print (sleep_in(False, True)) # True
print (sleep_in(True, True)) # True


'''
https://madplay.github.io/post/python-main-function
'''