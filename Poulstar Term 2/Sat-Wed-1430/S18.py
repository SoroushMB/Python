from turtle import Turtle,Screen

asghar = Turtle()
while True:
	shape = input("What shape do you want from me to draw(Square,Circle,Triangle,Rectangle,Hexagon)? ").title()
	if shape == "Square":	
		for i in range(4):
			asghar.fd(100)
			asghar.lt(90)
	elif shape == "Circle":
		asghar.circle(100)
	elif shape == "Triangle":
		for i in range(3):
			asghar.fd(100)
			asghar.lt(120)
	elif shape == "Rectangle":
		for i in range(2):
			asghar.fd(150)
			asghar.lt(90)
			asghar.fd(100)
			asghar.lt(90)
	elif shape == "Hexagon":
		for i in range(6):
			asghar.fd(100)
			asghar.lt(60)
	elif shape == "End":
		Screen().bye()
	else:
		print("You have entered a non-relative name!\nPlease try again!")
done()
