def VowelCount(str): 
  
	vowels = ['a', 'e', 'i', 'o', 'u']
	vowels_in_str = []

	for x in vowels:
		if x in str:
			vowels_in_str = vowels_in_str + [x]
	
	print vowels_in_str
	print len(vowels_in_str)
	
usertxt = raw_input("Some random text: ")
	
VowelCount(usertxt) 