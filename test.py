import math

def SqrEq(a_, b_, c_):

	if not isinstance(a_ , float):
		raise TypeError()
	try:
		D = b_**2 - 4*a_*c_
		if D < 0:
			x_r = -b_ / (2.0*a_)
			x_i = math.sqrt(-D) / (2.0*a_) 
			x1 = str(x_r) + " + " + str(x_i)
			x2 = str(x_r) + " - " + str(x_i)
		else:
			x1 = (-b_ + math.sqrt (D)) / (2.0 * a_)
			x2 = (-b_ - math.sqrt (D)) / (2.0 * a_)	
		return [x1, x2]
	except ZeroDivisionError:
		x = -c_ / b_
		return [x, None]

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print("-------------------------------------")
roots = SqrEq(a,b,c)
print("-------------------------------------")
print("X1: ", roots[0])
print("X2: ", roots[1])
