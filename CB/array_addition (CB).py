# Program Name: Array Addition
# Task Description: Take array of numbers and return the string true if any combination of numbers in the array can be added up to equal the largest number in the array, otherwise return the string false.
# Parameter: The array will not be empty, will not contain all the same elements, and may contain negative numbers.
# Example: If arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. 

def addition(arr):

	numbers = arr
	numbers.sort()
	print numbers
		
	a = -1
	b = 0

	#check if elements are the same - print error message	
	while numbers[b] != numbers[-1]:
		a += 1
		b += 1
		if numbers[a] == numbers[b]:
			print "There are duplicates in this list"
			break
	
	for x in numbers:
		if x == 0:
			print "true"
	
	#TO WORK ON: check combination of numbers added to equal largest number
	
	smaller_numbers = numbers[:-1] #all numbers except largest, combination of numbers to equal largest
	print "smaller numbers:", smaller_numbers

#automatically checks to see if list is empty	
user_txt = list(input("Numbers: "))	
addition(user_txt)