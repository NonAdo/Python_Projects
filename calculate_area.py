print "\nWelcome! This program calculates the area for simple shapes.\n "
def shapecalc():
	

	shape = raw_input ("What is your shape? ")

	#This asks the user for length and with and assigns it to 'l' and 'w'
	if shape == "rectangle":
		l = input ("what is the length of your rectangle? ")
		w = input ("what is the width of your rectangle? ")
		area_rect = l * w
		print "The area of your rectangle with length %s and width %s is %s" % (l, w, area_rect)

	#This asks the user for radius and assigns it to 'r'
	elif shape == "circle":
		r = input ("what is the radius of your circle? ")
		area_circ = 3.14 * (r ** 2)
		print "The area of your circle with radius %s is %s" % (r, area_circ)

	#This asks the user for base and height and assigns it to 'b' and 'h'
	elif shape == "triangle":
		b = input ("what is the base of your triangle? ") 
		h = input ("what is the height of your triangle? ")
		area_tri = b * h * .5
		print "The area of your triangle with %s and %s is %s" % (b, h, area_tri)
	else:
		print "Sorry, I can't calculate the area of your shape "
		
	run_func = raw_input("Do you have another shape with a mysterious area, yes or no? ")
	if run_func == "yes": 
		shapecalc()
	else:
		print "Ok, see you later slacker. "

shapecalc()
		


