"""
File: quadratic_solver.py
Name:傅冠鈞
-----------------------
This program implements a console-based solver for a
quadratic equation.

It asks the user to input three values a, b, and c,
and computes the roots of the equation:
ax^2 + bx + c = 0.

The output format should match the sample run shown
in the Assignment 2 handout.
"""

import math


def main():
	print("stanCode Quadratic Solver!")
	a = int(input("a: "))
	b = int(input("b: "))
	c = int(input("c: "))
	"""
	input 3個未知數
	"""
	if b*b-4*a*c > 0:
		x1 = ((-b) + math.sqrt(b*b - 4*a*c)) / (2*a)
		x2 = ((-b) - math.sqrt(b*b - 4*a*c)) / (2*a)
		print("Two roots: "+str(x1)+", "+str(x2))
		"""
		if 判別式>0，則帶入公式解解出2根
		"""
	elif b*b - 4*a*c == 0:
		x3 = (-b) / (2*a)
		print("One root: "+str(x3))
		"""
		if判別式=0，則(-b) / (2a)解出唯一1根
		"""
	else:
		print("No real roots")
		"""
		if判別式<0，則無實根
		"""


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
