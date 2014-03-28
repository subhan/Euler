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
    if number <= 1:
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
    if isinstance(num, type('')):
        if num.startswith('0'):
            ipdb.set_trace()
        return num == num[::-1].lstrip('0')
     
    return num == int(str(num).lstrip('0')[::-1])


def factors(num):
    upperlimit = int(num**0.5)
    seq = set()
    for i in range(1, upperlimit+1):
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


def sum_of_squares(seq):
    return sum([i**2 for i in seq])


def diff_between_sofsqs_sqsofs(seq):
    """
    #sofsqs : sum of squares
    #sqsofs : squares of sum
    >>> diff_between_sofsqs_sqsofs(range(1,11))
    2640
    >>> diff_between_sofsqs_sqsofs(range(1,101))
    25164150
    """
    return squares_of_sum(seq) - sum_of_squares(seq)
 
def greatest_product_of_consecutive_digit(numer, con_num = 5):
    """
    >>> greatest_product_of_consecutive_digit(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    40824
    """
    string_num = str(numer)
    end = len(string_num)
    maximum = 0
    for i in range(0, end):
        series = string_num[i:i+con_num]
        if len(series) < 5:
            return maximum 
        value = reduce(lambda x,y: x*y,
            [int(element) for element in series])
        #ipdb.set_trace()
        if maximum < value:
            maximum = value

if __name__ == "__main__":
    import doctest
    doctest.testmod()
