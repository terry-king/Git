# A simple calculator in Python
# University of the People 

import sys 
#First Number Input
num1 = input("Please enter the first number: ")

#Check for valid input (Greater than 0)
#Quit the program on error 

if num1 <1:
	print("\nError: Invalid number entered!")
	quit()	

else:
	print("\nFirst number entered")

# Second integer entry 
num2 = input("\nPlease enter the second number: ")

#Check for valid input for num2 (Greater than 0)
#Quit the program on error

if num2 <1:
	print("\nError: Invalid number entered!")
	quit()

else:
        print("\nSecond number entered")

#Operator input 
operator = raw_input("\nPlease enter math operator required (+, -, *, /")

# Operator selection and validation
# Make the calculation based on the selected operator
# Print the result 
if operator == '+':
	print('{} + {} = ' .format(num1, num2))
	print(num1 + num2)

elif operator == '-':
	print('{} - {} = ' .format(num1, num2))
	print(num1 - num2)

elif operator == '*':
	print('{} * {} =' .format(num1, num2))
	print(num1 * num2)

elif operator == '/':
	print('{} / {} = ' .format(num1, num2))
	print(num1 / num2)



# Error for incorrect operator entry, end program with error  
else:
	print('\nInvalid operator entered, please try again!')
	quit()
	