# Program Name: Scrambled Numbers
# Task Description:  Take the numbers being passed and return the next number greater than given number using the same digits. If a number has no greater permutations, return -1 (ie. 999). 
# Parameter: N/A
# Example: If num is 123 return 132, if it's 12453 return 12534.

import itertools

def permutation(num):

	numbers = list(user_txt)
	numbers = "".join(numbers)
	print numbers
	
	num_perms = []
	
	for x in set(itertools.permutations(numbers)):
		num_perms = num_perms + [(x)]
	
	# for y in num_perms:
	
	print num_perms
	
user_txt = raw_input("Number: ")
permutation(user_txt)