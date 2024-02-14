#!/usr/bin/python3
"""Module defines a method that returns winner of Prime Game
"""


def get_primes_len(n):
    """Returns the length of the prime numbers less than or equal to n
    Args:
        n: integer number
    Returns:
        The length of prime numbers
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return len(prime)


def isWinner(x, nums):
    """Return the winner of prime game
    Args:
        x: the number of rounds
        nums: an array of integers
    Returns:
       name of the player that won the most rounds
       None if the winner cannot be determined
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    numBenWon = 0
    numMariaWon = 0

    for i in range(x):
        if get_primes_len(nums[i]) % 2 == 0:
            numBenWon += 1
        else:
            numMariaWon += 1
    if numMariaWon > numBenWon:
        return 'Maria'
    elif numBenWon > numMariaWon:
        return 'Ben'
    return None
