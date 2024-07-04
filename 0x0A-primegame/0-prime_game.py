#!/usr/bin/python3
"""Module for Prime Game"""


def sieve_of_eratosthenes(max_num):
    """ Return a list where the index represents a potential prime number."""
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers
    p = 2
    while (p * p <= max_num):
        if (sieve[p] == True):
            # Marking the multiples of p as non-prime
            for i in range(p * p, max_num + 1, p):
                sieve[i] = False
        p += 1
    return sieve



def isWinner(x, nums):

    if x <= 0 or nums is None or x != len(nums):
        return None

    max_n = max(nums)
    primes_sieve = sieve_of_eratosthenes(max_n)

    ben_wins = 0
    maria_wins = 0

    for n in nums:
        if n <= 1:
            continue

        primes_count = sum(primes_sieve[:n + 1])

        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if ben_wins > maria_wins:
        return "Ben"
    elif maria_wins > ben_wins:
        return "Maria"
    else:
        return None
