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
    >>> all_amicable_numbers(10000)
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
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
