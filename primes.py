"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    with open('primes.txt', 'r') as p:
        for i in range(number_of_primes):
            prime = int(p.readline())
            list.append(prime)

    return list