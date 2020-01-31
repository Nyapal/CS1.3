#!python

import string
import math
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

hex_dict = {'10': 'a', '11': 'b', '12': 'c', '13': 'd', '14': 'e', '15': 'f', '16': 'g', '17' : 'h', '18': 'i', '19': 'j', '20': 'k',  '21': 'l', '22': 'm', '23': 'n', '24': 'o', '25': 'p', '26': 'q', '27': 'r', '28': 's', '29': 't', '30': 'u',  '31': 'v', '32': 'w', '33': 'x', '34': 'y', '35': 'z' }

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    result = 0 #Keep a running total
    i = 0
    reversed_digits = digits[::-1]

    for digit in reversed_digits:
        if digit.isalpha():
            for key, value in hex_dict.items(): 
                    if value == digit:
                        digit = key

        output= (base**i)
        total = int(digit) * output
        result += total
        i += 1    
    return result


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    
    encode_dict = string.digits + string.ascii_lowercase
    #list to hold converted characters
    output = []

    while number != 0:
        remainder = number % base
        quotient = number//base
        number = quotient
        
        #new hex digit
        hex_digit = encode_dict[remainder]
        #insert hex digit into output list
        output.insert(0, str(hex_digit))

    return ''.join(output)


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    
    result = decode(digits, base1)
    return encode(result, base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
