# Program Name: Palindrome I
# Task Description:  Return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false.
# Parameter: Punctuation and numbers will not be part of the string.
# Example: "racecar" is also "racecar" backwards.

import string

def is_palindrome(str):

	str = ''.join([x for x in str if x.isalpha()])
	print str
	reverse_str = str[::-1]
	
	if str == reverse_str:
		print "true"
	else:
		print "false"

user_txt = raw_input("Palindrome check: ")
is_palindrome(user_txt)

#http://coderbyte.com/CodingArea/Editor.php?ct=Palindrome&lan=Python