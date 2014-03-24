import ipdb 
import solutions

def get_amicable_pair(num):

    a = list(solutions.factors(num))
    a.remove(num)
    a = sum(a)
 
    b = list(solutions.factors(a))
    b.remove(a)
    b = sum(b)

    if b == num and a != b:
        return a, b
    return None


def sum_of_all_amicable_numbers(limit):
    """
    >>> sum_of_all_amicable_numbers(10000)
    31626
    """
    items = [] 
    for num in range(1, limit):
        if num in items or solutions.is_prime(num):
            continue
        result = get_amicable_pair(num)
        if result:
            a, b = result
            if a not in items:
                items.append(a)
            if b not in items:
                items.append(b)
    return sum(items)
            

def lenth_of_fib(length):
    index = 1
    while True:
        val = solutions.fib(index)
        if len(str(val)) == length:
            return val 
        index += 1


def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]


def list_to_num(items):
    return "".join([str(i) for i in items])


def nth_permutation(series, nth):
    #permute_obj = permute(series, len(series))
    permute_obj = permute(series)
    index = 1
    #fl_obj = open('/tmp/combinations.txt', 'w')
    items = [] 
    while True:
        value = permute_obj.next()
        #fl_obj.write('%s\n'%value)
        items.append(list_to_num(value))
        if index == nth:
            break
        index += 1
    return items
    #fl_obj.close()


def first_fib_limit(limit):
    """
    >>> first_fib_limit(100)
    476
    >>> first_fib_limit(3)
    12
    >>> first_fib_limit(1)
    1
    """
    cached = {}
    index = 1
    while True:
        val = solutions.fib(index, cached)
        if len(str(val)) == limit:
            return index 
        cached[index] = val
        index += 1


def get_recurring_number(val):
    val = str(val).split('.')[1]
    num_str = ''
    for c in val:
        if c in num_str:
            return num_str
        num_str += c
         

def longest_recurring_decimal_fraction(limit):
    
    for index in range(2, limit): 
        val = 1/float(index)
        print get_recurring_number(val)       


def is_abundant_number(num):
    factors = list(solutions.factors(num))
    factors.remove(num)
    return sum(factors) > num


def abundant_generator(seed=None):
    i = seed or 12
    while True:
        if is_abundant_number(i):
            yield i
        i += 1


def is_sum_of_2abundant(num):
    if num < 24:
        return False
    elif num == 24:
        return True
    abundant_gen = abundant_generator()
    val = abundant_gen.next()
    smallest_abundant = 12
    while True:
        remaining = num - val
        if remaining == val or remaining == smallest_abundant:
            return True
        elif remaining < smallest_abundant:
            return False 
        elif is_abundant_number(remaining):
            return True
        val = abundant_gen.next()


def non_abundant_sum(limit=28123):
    """
    >>> non_abundant_sum()
    4179871
    """
    return sum([i for i in xrange(limit+1) if not is_sum_of_2abundant(i)])

 
if __name__ == '__main__':
    import doctest
    doctest.testmod()
