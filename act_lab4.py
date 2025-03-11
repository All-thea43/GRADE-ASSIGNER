def assign_grade(score):
	print("This will assign a letter grade based on your score.")
	
while True:
	try:
		grade = int(input("Input your assign grade score: "))
		if grade >= 90:
			print("Grade: A")
		elif grade >= 80:
			print("Grade: B")
		elif grade >= 70:
			print("Grade: C")
		elif grade >= 60:
			print("Grade: D")
		elif grade < 0 or grade > 100:
			print("Invalid score! Please enter a value between 0 and 100. ")
		else:
			print("Grade: F")
	except ValueError:
		print("Invalid score! Please enter a numerical value. ")
			