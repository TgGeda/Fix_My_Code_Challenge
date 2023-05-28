#!/usr/bin/python3
""" FizzBuzz
"""
import sys

def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if n < 1:
        return
    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./fizzbuzz.py <number>")
        print("Example: ./fizzbuzz.py 89")
        sys.exit(1)
    number = int(sys.argv[1])
    fizzbuzz(number)
    
# The code has the wrong condition for checking for multiples of 3 and 5 (and printing FizzBuzz). 
# The elif condition for multiples of both three and five was placed before the if condition for multiples of three which was causing the program to print only Fizz for multiples of both three and five. 
# I also corrected the usage message by removing the leading './0-' in the script name.
