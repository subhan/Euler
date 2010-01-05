
def sumof35(n):
	"""
	>>> sumof35(10)
	23
	"""
	sum = 0
	for i in range(1,n):
		sum += (i%3==0 or i%5==0) and i or 0
	return sum


def fib(n,cache={}):
	"""
	>>> fib(1)
	1
	>>> fib(5)
	8
	"""
	if n == 1 or n == 2:
		return n
	elif  n in cache:
		return cache[n]
	else:
		cache[n] = fib(n-1,cache)+fib(n-2,cache)
		return cache[n]
	
def generate_fibSeries(n):
	i,l = 1,[]
	cache = {}
	while True:
		f = fib(i,cache)
		if f < n:
			l.append(f)
			i += 1
		else:
			break
	return l

def sumOfFibs(list):
	"""
	>>> sumOfFibs(filter(lambda x:x%2==0,generate_fibSeries(4000000)))
	4613732
	"""
	return reduce(sum,list)

if __name__ == "__main__":
	import doctest
	doctest.testmod()
