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
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[total] if dp[total] != float('inf') else -1
