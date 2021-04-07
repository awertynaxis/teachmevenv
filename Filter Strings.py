strings = [
    'Abrakadabra',
    'Abc Abc B',
    'Abc Abc Abc',
    'Chapter 1: Abrakadabra',
    'abc abc abc',
    'awd',
    ]

def filter(sequence:list, condition)->list:
    """
    :param sequence input list of strings wich we will be checked by functions in condition
    :param condition input function wich checks input sequence
    returns list of strings which are valid for conditions
    """
    filter_1=[]
    if condition==has_three_a:
        for item in sequence:
            if has_three_a(item) == True:
                filter_1.append(item)
    else:
        for item in sequence:
            if is_alpha_title(item) == True:
                filter_1.append(item)
    return filter_1

def has_three_a(item:str)->bool:
    """
    >>> has_three_a('Anaconda') #we get a string on entrance wich has 3 vowels a
    True
    >>> has_three_a('Millyways')# we get a string wich hasnt 3 a vowels and result must be None
    None
    this function checks a number of vowels a,A in word
    :param item entrance string
    """
    j=0
    for x in item:
        if x in ['a','A']:
            j+=1
    if j>=3:
        return True


def is_alpha_title(item:str)->bool:
    """
    :param item entrance string
    This function gets string and checks: is there 'A' in string?
    """
    a='A'
    if item[0] == a:
        return True



assert filter(strings, has_three_a) == ['Abrakadabra', 'Abc Abc Abc', 'Chapter 1: Abrakadabra', 'abc abc abc',]
assert filter(strings, is_alpha_title) == ['Abrakadabra', 'Abc Abc B', 'Abc Abc Abc',]