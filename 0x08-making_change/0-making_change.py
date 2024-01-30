#!/usr/bin/python3
"""Module defines a method that returns fewest number of coins
    needed to meet total
"""


def makeChange(coins, total):
    """Return fewest number of coins needed to meet total
    Args:
        coins: a list of the values of the coins in your possession
        total: given amount
    Returns:
        0 - if total is 0 or less,
        -1 - If total cannot be met by any number of coins
    """
    if total <= 0:
        return 0
    if coins == [] or coins is None:
        return -1
    try:
        n = coins.index(total)
        return 1
    except ValueError:
        pass

    coins.sort(reverse=True)
    coin_count = 0
    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count = total // coin
            coin_count += count
            total -= count * coin
    if total > 0:
        return -1
    return coin_count
