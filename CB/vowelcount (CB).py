def VowelCount(str): 
  
	vowels = ['a', 'e', 'i', 'o', 'u']
	vowels_in_str = []

	count = 0
	
	for x in str:
		for y in vowels:
			if x == y:
				count += 1

	print count
	
usertxt = raw_input("Some random text: ")
VowelCount(usertxt)