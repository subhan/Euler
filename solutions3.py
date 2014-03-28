import solutions
import solutions2
import ipdb

def change(money, options=None):
    changes = [ ]
    options = options or [1, 2, 5, 10, 20, 50, 100]
    def make_change(money, coins):
        for count in options:
            if money - count < 0:
                return 
            elif money - count == 0:
                val = sorted(coins + [count])
                if val not in changes:
                    print val
                    changes.append(val)
                    return
            else:
                make_change(money - count, coins+[count])
        return changes
    return make_change(money, [])

def get_digits(num):
    digits = []
    while num:
        digits.append(num % 10)
        num /= 10
    return digits

def list_to_num(items, reverse=True):
    multiplier = 1
    total = 0 
    for item in items[::-1]:
        total += item*multiplier
        multiplier *= 10
    return total
        
def get_circular_digits(num):
    original = get_digits(num)[::-1]
    temp = original[1:] + [original[0]]
    result = [original] 

    while temp != original:
        result.append(temp)
        temp = temp[1:] + [temp[0]]     
    return result

def is_circular_prime(num):

    for item in get_circular_digits(num):
        if not solutions.is_prime(list_to_num(item)):
            return False
    return True 

def convert_to_base(num, base=2):
    _repr = ''
    while num:
        _repr += str(num % base)
        num /= base 
    return _repr[::-1]

def is_palindrome(num, base=True):
    """
    >>> is_palindrome(585)
    True
    """
    if not solutions.is_palindrome(num):
        return False 
    return solutions.is_palindrome(convert_to_base(num)) 

def truncatable_prime(num):
    digit = solutions.get_digits(num)
    divisor = 1
    while num/divisor:
        val = num / divisor
        if not solutions.is_prime(val) or val == 1:
            return False
        val = num % divisor
        if val == 1:
            return False
        elif val > 0 and not solutions.is_prime(val):
            return False
        divisor *= 10

    return True

def generate_truncatable_prime():
    i = 11
    while True:
        if truncatable_prime(i):
            yield i
        i += 2


if __name__ == '__main__':
    import doctest
    doctest.testmod()
