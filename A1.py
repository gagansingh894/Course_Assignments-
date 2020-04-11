import math

# Q1
for num in range(2000,3200):
	if (num % 7 == 0) & (num / 5 != 1):
		print(num, end=',')

print()

# Q2

fnInput = input("Enter First Name: ")
lnInput = input("Enter Last Name: ")
print("Result: {0} {1}". format(lnInput, fnInput))

print()

# Q3

def Volume_Sphere(r):
	vol =  4/3 * math.pi * r ** 3
	print("The volume of sphere is: {}".format(vol))

Volume_Sphere(2)
print()

# Q4

inputValues=input('Please Input Comma Seperated Values: ')
list=inputValues.split(',')
print(list)
print()

# Q5
for i in range(7):
	for j in range(i):
		print("*", end="")
	print()
for i in range(7,0,-1):
	for j in range(i):
		print("*", end="")
	print()

print()

# Q6

inputWord = input("Please enter a word: ")
print("The required output is: {}".format(inputWord[::-1]))

# Q7

inputSTR = "WE, THE PEOPLE OF INDIA, {}having solemnly resolved to constitute India into a SOVEREIGN,{} SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC {} and to secure to all its citizens"
print(inputSTR.format('\n\t','!\n\t\t','\n\t\t'))
