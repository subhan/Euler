import ipdb

def sumof35(number):
    """
    >>> sumof35(10)
    23
    """
    total = 0
    for i in range(1, number):
        total += (i%3==0 or i%5==0) and i or 0
    return total


def fib(number, cache=None):
    """
    >>> fib(1)
    1
    >>> fib(5)
    8
    """
    cache = cache or {}
    if number == 1 or number == 2:
        return number
    elif  number in cache:
        return cache[number]
    else:
        cache[number] = fib(number-1, cache) + fib(number-2, cache)
        return cache[number]


def generate_fibseries(number):
    i, seq = 1, []
    cache = {}
    while True:
        val = fib(i, cache)
        if val < number:
            seq.append(val)
            i += 1
        else:
            break
    return seq


def sum_of_fibs(items):
    """
    >>> sum_of_fibs(filter(lambda x:x%2==0, generate_fibseries(4000000)))
    4613732
    """
    return reduce(lambda x, y: x+y, items)


def is_prime(num):
    upperlimit = int(num ** 0.5)
    if num in (1, 2):
        return True
    if num % 2 == 0:
        return False
    lowerlimit = 3
    while lowerlimit <= upperlimit:
        if num % lowerlimit == 0:
            return False
        lowerlimit += 2
    return True


def generate_primefactors(num, primes=None):
    primes = primes or []
    facts = sorted(factors(num))
    items = facts[1:-1]    
    if items: 
        for item in items:
            if is_prime(item):
                primes.append(item)
            else:
                generate_primefactors(item, primes)
    elif facts[0] not in primes:
        primes.append(facts[0])
    return primes


def largest_prime_factor(num):
    return max(generate_primefactors(num))


def get_digits(num):
    """
    >>> get_digits(3354)
    4
    """
    total = 0
    while num:
        num /= 10
        total += 1
    return total


def is_palindrome(num):
    """
    >>> is_palindrome(121)
    True
    """
    return num == int(str(num)[::-1])

def factors(num):
    upperlimit = int(num**0.5)
    seq = [] 
    for i in range(1, upperlimit+1):
        if num % i == 0:
            seq.append(i)
            seq.append(num/i)
    return seq

def generate_palindrome(start, end):
    seq = []
    while start <= end:
        if is_palindrome(start):
            seq.append(start)
            start += 10
        else:
            start += 1
    return seq


def largest_palindrom_multiples_of_digits(digits):
    """
    >>> largest_palindrom_multiples_of_digits(3)
    906609
    """
    start = (10**(digits-1))
    end = (10**digits-1)
    palindromes = generate_palindrome(start**2, end**2)

    large = 0
    for palindrome in palindromes:
        val = max([x for x in factors(palindrome) if x >= start and x <= end] or [0])
        if val and get_digits(palindrome/val) == 3 and large < palindrome:
            large = palindrome
    return large


def continues_series_count(values):
    filtered_values = set(values)
    data = {}

    for item in filtered_values:
        for val in values:
            if item == val:
                if item in data:
                    data[item] += data.get(item)
                else:
                    data[item] = 1
            elif item in data:
                del data[item] 
    return data


def smallest_multiple(start, end):
    """
    #>>> smallest_multiple(1, 21):
    #232792560
    """
    primes = {}
    for i in range(start, end):
        update_count(primes, generate_primefactors(i) or [i])
    ipdb.set_trace()

def sum_of_squares(seq):
    return sum([i**2 for i in seq])

def generate_prime():
    i = 2
    while True:
        if is_prime(i):
            yield i
        i += 1

def prime_index(index):
    """
    >>> prime_index(10001)
    104743
    >>> prime_index(6)
    13
    """
    i = 1
    prime_generator = generate_prime()
    while True:
        prime_numer = prime_generator.next()
        if i == index:
            return prime_numer
        i += 1
        
def squares_of_sum(seq):
    return sum(seq) ** 2


def diff_between_sofsqs_sqsofs(seq):
    """
    >>> diff_between_sofsqs_sqsofs(range(1,11))
    2640
    >>> diff_between_sofsqs_sqsofs(range(1,101))
    25164150
    """
    return squares_of_sum(seq) - sum_of_squares(seq)
 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
