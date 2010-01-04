
def sumof35(n):
	"""
	>>> sumof35(1000)
	23
	"""
	sum = 0
	for i in range(1,n):
		sum += (i%3==0 or i%5==0) and i or 0
	return sum

if __name__ == "__main__":
	import doctest
	doctest.testmod()
