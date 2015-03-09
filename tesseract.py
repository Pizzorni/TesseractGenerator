import turtle

def main():
	print('Welcome to the super awesome Turtle Tesseract Generator 9000!\n')
	print('Please input a number between 2 and 6')
	r = input('Enter square length:')
	#Draw initial Square

	rad = 20.0*r
	scr = turtle.Screen()
	tess = turtle.Turtle()
	scr.setup(width=1.0, height=1.0, startx=0, starty=0)
	# Draw initial square
	v = [[0,0]]
	v.append([0,rad])
	v.append([rad,rad])
	v.append([rad,0])
	tess.setpos(v[1])
	tess.setpos(v[2])
	tess.setpos(v[3])
	tess.setpos(v[0])
	tess.setpos(v[3])

	## Draw corner extensions ##

	#Bottom Right Corner
	v.append([3*rad/2, 0])
	v.append([rad, -rad/2])
	tess.setpos(v[4])
	tess.setpos(v[3])
	tess.setpos(v[5])
	tess.penup()
	
	#Bottom Left Corner
	v.append([0, -rad/2])
	v.append([-rad/2, 0])
	tess.setpos(v[0])
	tess.pendown()
	tess.setpos(v[6])
	tess.setpos(v[0])
	tess.setpos(v[7])
	tess.penup()

	#Upper Left Corner
	v.append([-rad/2, rad])
	v.append([0, 3* rad/2])
	tess.setpos(v[1])
	tess.pendown()
	tess.setpos(v[8])
	tess.setpos(v[1])
	tess.setpos(v[9])
	tess.penup()

	#Upper Right Corner
	v.append([rad, 3*rad/2])
	v.append([3*rad/2, rad])
	tess.setpos(v[2])
	tess.pendown()
	tess.setpos(v[10])
	tess.setpos(v[2])
	tess.setpos(v[11])
	

	v.append([3*rad/2, 3*rad]) #12
	v.append([-rad/2, 3*rad])  #13
	v.append([3*rad, -rad/2])  #14
	v.append([3*rad, 3*rad/2])  #15
	v.append([-rad/2, -2*rad])  #16
	v.append([3*rad/2, -2*rad])  #17
	v.append([-2*rad, 3*rad/2])  #18
	v.append([-2*rad, -rad/2])  #19

	tess.setpos(v[14])
	tess.setpos(v[15])
	tess.setpos(v[12])
	tess.setpos(v[13])
	tess.setpos(v[18])
	tess.setpos(v[19])
	tess.setpos(v[16])
	tess.setpos(v[17])
	tess.setpos(v[14])
	tess.setpos(v[15])
	tess.setpos(v[4])
	tess.setpos(v[9])
	tess.setpos(v[12])
	tess.setpos(v[13])
	tess.setpos(v[10])
	tess.setpos(v[7])
	tess.setpos(v[18])
	tess.setpos(v[19])
	tess.setpos(v[8])
	tess.setpos(v[5])
	tess.setpos(v[16])
	tess.setpos(v[17])
	tess.setpos(v[6])
	tess.setpos(v[19])
	tess.setpos(v[6])
	tess.setpos(v[11])
	tess.setpos(v[14])
	tess.setpos(v[5])
	tess.setpos(v[10])
	tess.setpos(v[15])
	tess.setpos(v[4])
	tess.setpos(v[17])
	tess.setpos(v[16])
	tess.setpos(v[7])
	tess.setpos(v[18])
	tess.setpos(v[9])


	scr.exitonclick()

main()