# Program Name: Words Longer Than X
# Task Description: Takes a list of words and an integer n and return the list of words that are longer than n.
# Parameter: N/A
# Example: N/A
# Note: Problem 16

def filter_long_words(n, sentence):

	txt = sentence.split(" ")
	print txt

	x = -1
	
	while x != txt[-1]:
		x += 1
		print len(txt[x])	
	
user_txt = raw_input("Sentence: ")
user_num = int(raw_input("Number: "))

filter_long_words (user_num, user_txt)

#http://www.ling.gu.se/~lager/python_exercises.html