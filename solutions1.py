import ipdb
import json 
import string
import solutions 

def is_pythagorean_triplet(a, b, c):
    return a**2 + b ** 2 == c ** 2 and a < b and b < c


def special_pythagorean_triplet(n):
    """
    >>> special_pythagorean_triplet(12)
    3 4 5
    >>> special_pythagorean_triplet(1000)
    200 375 425

    A Pythagorean triplet is a set of three natural numbers,
    a < b < c, for which, a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.
    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    """
    for a in range(0, n/2):
        for b in range(a+1, n/2):
            for c in range(b+1, n/2):
                if a + b + c == n and is_pythagorean_triplet(a, b, c):
                    print a, b, c 

def sum_of_primes(limit):
    """
    >>> sum_of_primes(2000000)
    142913828922
    """ 
    sum = 0
    for prime in solutions.generate_prime():
        if prime < limit:
            sum += prime
        else:
            break
    
    return sum

def add_pointers(grid):
    new_grid = {}
    i = 0
    for line in grid:
        j = 0
        for ele in line:
            new_grid[(i,j)] = ele
            j += 1      
        i += 1
    return new_grid

def largest_product_in_grid(num):
    grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8], [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0], [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65], [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91], [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80], [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50], [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70], [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21], [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72], [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95], [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92], [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57], [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58], [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40], [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66], [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69], [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36], [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16], [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54], [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]

    original = grid

    grid = add_pointers (grid)
    maximum = 0
    limit = (len(original)-num) + 1
    for i in range(limit):
        for j in range(limit):
            k = 0
            total = 1
            items = []
            while k < num:
                total *= grid[(i+k, j+k)]
                items.append(grid[(i+k, j+k)])
                if maximum < total:
                    maximum = total
                k += 1
            print items

    import ipdb
    ipdb.set_trace()

def triangle_number_generator():
    i = 1
    total = 0
    while True:
        total +=i 
        yield total
        i += 1

def max_triangle_divisors(limit):
    """
    >>> max_triangle_divisors(500)
    76576500
    """
    triangle_number = triangle_number_generator()
    while True:
        value = triangle_number.next()
        factors = solutions.factors(value)
        if len(factors)-1 >= limit:
            return value

def get_collatz_seq(num, items=None):
    """
    >>> get_collatz_seq(13)
    [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    """
    items = items or []
    items.append(num)
    if num == 1:
        return items
    elif  num % 2 == 0:
        return get_collatz_seq(num/2, items) 
    else:
        return get_collatz_seq((3*num)+1, items) 


def longest_collatz_seq(limit):
    """
    >>> longest_collatz_seq(1000000)
    837799
    """
    longest = 0
    start = limit/2 
    last = 0
    while  start < limit:
        length = len(get_collatz_seq(start))
        if longest < length:
            longest = length
            last = start
        start += 1
    return last 


def power_digit_sum(num, power):
    """
    >>> power_digit_sum(2, 15)
    26
    """    
    result = num ** power
    total = 0
    while True:
        total += result % 10
        if result/10 == 0:
            return total
        result /= 10


def names_scores():
    i = 1
    alpha_char = {}
    for c in string.ascii_uppercase:
        alpha_char[c] = i
        i += 1 
    data = open('names.txt').read()
    names = sorted([i.strip().replace('"','') for i in data.split(',')])
    name_indexs = dict(enumerate(names, 1))
    names_score_map = {}
    for index, name in name_indexs.iteritems():
        total = 0
        for c in name:
            total += alpha_char[c]
        names_score_map[name] = total * index

    return names_score_map

dt = {
    'One' : 3, 'Two' : 3, 'Three' : 5, 'Four' : 4, 'Five' : 4, 'Six' : 3, 'Seven' : 5, 'Eight' : 5, 'Nine' : 4, 'Ten' : 3,
    'Eleven' : 6, 'Twelve' : 6, 'Thirteen' : 8, 'Fourteen' : 8, 'Fifteen' : 7, 'Sixteen' : 7, 'Seventeen' : 9, 'Eighteen' : 8,
    'Nineteen' : 8, 'Twenty' : 6, 'Thirty' : 6, 'Forty' : 5, 'Fifty' : 5, 'Sixty' : 5, 'Seventy' : 7, 'Eighty' : 6,
    'Ninety' : 6, 'Hundred' : 7, 'Thousand' : 8 
}

num_to_word = {
    1:'One' , 2:'Two' , 3:'Three' , 4:'Four' , 5:'Five' , 6:'Six' , 7:'Seven' , 8:'Eight' , 9:'Nine' , 10:'Ten',
    11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen',
    19:'Nineteen', 20:'Twenty', 30:'Thirty', 40:'Forty', 50:'Fifty', 60:'Sixty', 70:'Seventy', 80:'Eighty',
    90:'Ninety', 100:'Hundred',  1000: 'Thousand'
}

def print_it(num_seq):

    result = []
    for num in num_seq:
        if isinstance(num, type(())):
            result.append(num_to_word[num[0]])
            result.append(num_to_word[num[1]])
        elif str(num).find('00') >= 1:
            result.append('One '+num_to_word[num])
        else:
            result.append(num_to_word[num])
    return result

def num_to_words(num, items = None):
    items = items or []
    if num in num_to_word:
        items.append(num) 
        return items

    digit = solutions.get_digits(num)
    nth = 10**(digit-1)
    div = num / nth
    rem = num % nth
    if div*nth in num_to_word:
        items.append(div*nth)
    else:
        items.append((div, nth))

    if rem in num_to_word:
        items.append(rem)
    elif rem >= 1:
        num_to_words(rem, items)

    return items


def covert_into_words(num):
    items = num_to_words(num)
    return print_it(items)


def count_it(seq):
    total = 0
    for item in seq:
        if isinstance(item,type(())):
            total += dt[num_to_word[item[0]]]
            total += dt[num_to_word[item[1]]]
        elif str(item).find('00') >= 1:
            total += 3
            total += dt[num_to_word[item]]
        else:
            total += dt[num_to_word[item]]
    if len(seq) > 2:
        total += 3
    elif len(seq) == 2:
        if isinstance(seq[0], type(())) or isinstance(seq[1], type(())):
            total += 3
        elif seq[0] >= 100:
            total += 3
    return total


def number_letter_counts(num):
    """
    >>> number_letter_counts(1000)
    21124
    """
    total = 0
    for num in range(1, num+1):
        total += count_it(num_to_words(num))
    return total


def factorial(num):
    """
    >>> factorial(10)
    3628800
    """
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)


def factorial_digit_sum(n):
    """
    >>> factorial_digit_sum(10)
    27
    """
    return sum([int(i) for i in str(factorial(n))])
 

if __name__ == "__main__":
    import doctest
    doctest.testmod()
