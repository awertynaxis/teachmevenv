from math import sqrt


def is_square(item: int) -> bool:
    '''
    >>>is_square(16)#if we enter a integer number 16 it returns True
    True
    >>>is_square(5)#if we enter a integer number 5 it returns None
    None
    this function gets a number and returns only wich number is square
    :param item: integer number wich checks in functions
    '''
    if sqrt(item).is_integer() and item!=0:
        return True


def is_prime(item:int)->bool:
    """
    gets a number and returns a prime number
    >>>is_prime(11)#if entered number is prime returns True
    True
    >>>is_prime(6)#if entered number has more then 2 dividers it returns None
    None
    :param item: integer number wich checks in functions
    """
    i = 2
    while i <= sqrt(item):
         if item % i == 0:
            break
         i += 1
    return i > sqrt(item) and item!=0



def filter(sequence:int,condition)->list:
    """
    This function gets a sequence of numbers and checks condition depends on wich function is called
    :param sequence:a list of numbers
    :param condition: function will procces a entered list of numbers
    """
    suitiable_items=[]
    for item in sequence:
        if condition(item):
            suitiable_items.append(item)
    return suitiable_items


assert filter(range(25), is_square) == [1, 4, 9, 16]
assert filter(range(25), is_prime) == [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
