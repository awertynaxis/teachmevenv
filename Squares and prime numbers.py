from math import sqrt


def is_square(item: int) -> bool:
    '''this function gets a number and
        returns only wich number is square'''

    if sqrt(item).is_integer() and item!=0:
        return True


def is_prime(item:int)->bool:
    """gets a number and returns a prime number"""
    i = 2
    while i <= sqrt(item):
         if item % i == 0:
            break
         i += 1
    if i > sqrt(item) and item!=0:
           return True

def filter(sequence:int,is_prime)->list:
    """This function just returns result of too functions : is_square and is_prime"""
    filter_1=[]
    filter_2=[]
    for item in sequence:
            if is_square(item)==True:
             filter_1.append(item)
            if is_prime(item) == True:
                filter_2.append(item)
    return filter_2

assert filter(range(25), is_square) == [1, 4, 9, 16]
assert filter(range(25), is_prime) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
