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
    while lowerlimit < upperlimit:
        if num % lowerlimit == 0:
            return False
        lowerlimit += 2
    return True


def generate_primefactors(num, primes=None):
    primes = primes or []
    facts = list(factors(num))
    if len(facts) == 1:
        primes.append(num)
        return primes
    for item in facts:
        if is_prime(item):
            primes.append(item)
        else:
            generate_primefactors(item, primes)
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
    seq = set()
    seq.add(1)
    for i in range(2, upperlimit+1):
        if num % i == 0:
            seq.add(i)
            seq.add(num/i)
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


def update_count(data, values):
    for val in values:
        if val in data:
            data[val] += 1
        else:
            data[val] = 1


def smallest_multiple(start, end):
    """
    #>>> smallest_multiple(1, 21):
    #232792560
    """
    primes = {}
    for i in range(start, end):
        update_count(primes, generate_primefactors(i) or [i])
    import ipdb
    ipdb.set_trace()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
