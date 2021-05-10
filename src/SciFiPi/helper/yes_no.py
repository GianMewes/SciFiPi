def yes_no(answer):
	yes = set(['y'])
	no = set(['n'])
	 
	while True:
		choice = input(answer).lower()
		if choice in yes:
		   return True
		elif choice in no:
		   return False
		else:
		   print("Please respond with 'y' or 'n' ")