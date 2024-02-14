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
    primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
            primes.append(num)
    return len(primes)


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

    for i in range(len(nums)):
        if get_primes_len(nums[i]) % 2 == 0:
            numBenWon += 1
        else:
            numMariaWon += 1
    if numMariaWon > numBenWon:
        return 'Maria'
    elif numBenWon > numMariaWon:
        return 'Ben'
    return None
