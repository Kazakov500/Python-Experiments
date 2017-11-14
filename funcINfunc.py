def func_old1(selector):
	if selector < 0 :
		def func1(x):
			return x*x
		return func1
	else:
		def func2(x):
			return x*x*x
		return func2

def oper_old1(L, function):
	res = []
	for K in L:
		res.append(function(K))
	return res
#----------------------------------------

def func(selector):
	if selector < 0 :
		return lambda x: x*x
	else:
		return lambda x: x*x*x


def oper(L, function):
	return [function(K) for K in L]



X = [1,2,3,4]
print (X)
print (oper(X, func(-1)))
print (oper(X, func(1)))
