import os
import string
import random
from string import digits


def idv3(size=13, chars=digits):
    return int(''.join(random.choice(chars) for _ in range(size)))


def idv1(size=10, chars=digits):
    return int(''.join(random.choice(chars) for _ in range(size)))




def generate_random_string(length, stringset=string.ascii_letters+string.digits+string.punctuation):
    """
    Returns a string with `length` characters chosen from `stringset`
    >>> len(generate_random_string(20) == 20 
    """
    return ''.join([stringset[i%len(stringset)] for i in [x for x in os.urandom(length)]])
