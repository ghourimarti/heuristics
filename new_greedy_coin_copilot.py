#!/usr/bin/env python

"""
Greedy Coin Change Algorithm
1. The function greedy_coin takes one argument, the amount of change to be given to the customer.
2. The function prints a statement to tell the customer how much change they are getting.
3. The function initializes a list of coins (quarters, dimes, nickels, and pennies) and a dictionary that maps the coins to their denominations.
4. The function initializes a dictionary that will hold the number of coins of each type.
5. The function goes through the list of coins and initializes the dictionary with a value of 0 for each coin.  
"""
import click


# <------------------------------------------------------------------->
# <---------------------------- All coins ---------------------------->
# <------------------------------------------------------------------->
# build a function to find minimum number of coins
# using quarters, dimes, nickels and pennies
def greedy_coin(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""

    print(f"Your change for {change}: ")
    coins = [0.25, 0.10, 0.05, 0.01]
    coin_lookup = {0.25: "quarter", 0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    print(coin_dict)
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin_dict


# <------------------------------------------------------------------->
# <---------------------- Quarters and Dimes -------------------------->
# <------------------------------------------------------------------->
# build a greedy algorithm to find the minimum number of coins
# but only use quarters, dimes
def greedy_coin_qd(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""

    print(f"Your change for {change}: ")
    coins = [0.25, 0.10]
    coin_lookup = {0.25: "quarter", 0.10: "dime"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    print(coin_dict)
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin


# <------------------------------------------------------------------->
# <----------------- Pennies, Nickels and Dimes ----------------------->
# <------------------------------------------------------------------->
# build a greedy algorithm to find the minimum number of coins
# but only use pennies, nickels and dimes
def greedy_coin_pnd(change):
    """Return a dictionary with the coin type as the key and the number of coins as the value"""

    print(f"Your change for {change}: ")
    coins = [0.10, 0.05, 0.01]
    coin_lookup = {0.10: "dime", 0.05: "nickel", 0.01: "penny"}
    coin_dict = {}
    for coin in coins:
        coin_dict[coin] = 0
    print(coin_dict)
    for coin in coins:
        while change >= coin:
            change -= coin
            coin_dict[coin] += 1
    for coin in coin_dict:
        if coin_dict[coin] > 0:
            print(f"{coin_dict[coin]} {coin_lookup[coin]}")
    return coin


# <------------------------------------------------------------------->
# <------------------------ Click Group ------------------------------>
# <------------------------------------------------------------------->
# build a click group
# explain the function in detail
"""
1. The function main is a click group that takes no arguments.
2. The function main has a subcommand called greedy that takes one argument, the amount of change to be given to the customer.
3. The function main calls the greedy_coin function with the change argument.
"""


@click.group()
def main():
    """Return the minimum number of coins for a given change

    Example: ./greedy_coin.py 0.99
    """
    pass


# <------------------------------------------------------------------->
# <------------------------ Click Commands --------------------------->
# <------------------------------------------------------------------->
# build click commands
# explain the function in detail
"""
1. The function greedy is a click command that takes one argument, the amount of change to be given to the customer.    
2. The function greedy calls the greedy_coin function with the change argument.
"""


@main.command("greedy")
@click.argument("change", type=float)
def greedy(change):
    """
    Return the minimum number of coins for a given change
    example: ./new_greedy_coin_copilot.py greedy 0.99
    """
    greedy_coin(change)


# <------------------------------------------------------------------->
# <------------------------ Click Commands --------------------------->
# <------------------------------------------------------------------->
# build click commands
# explain the function in detail
"""
1. The function qd is a click command that takes one argument, the amount of change to be given to the customer.
2. The function qd calls the greedy_coin_qd function with the change argument.
"""


@main.command("qd")
@click.argument("change", type=float)
def qd(change):
    """
    Return the minimum number of coins for a given change
    using only quarters and dimes
    example: ./new_greedy_coin_copilot.py qd 0.99
    """
    greedy_coin_qd(change)


# <------------------------------------------------------------------->
# <------------------------ Click Commands --------------------------->
# <------------------------------------------------------------------->
# build click commands
# explain the function in detail
"""
1. The function nd is a click command that takes one argument, the amount of change to be given to the customer.
2. The function nd calls the greedy_coin_pnd function with the change argument.
"""


@main.command("pnd")
@click.argument("change", type=float)
def nd(change):
    """
    Return the minimum number of coins for a given change
    using only pennies, nickels and dimes
    example: ./new_greedy_coin_copilot.py pnd 0.99
    """
    greedy_coin_pnd(change)


# <------------------------------------------------------------------->
# <------------------------ Click Commands --------------------------->
# <------------------------------------------------------------------->
# build click commands
# explain the function in detail
"""
1. The function all is a click command that takes one argument, the amount of change to be given to the customer.
2. The function all calls the greedy_coin function with the change argument.
3. The function all calls the greedy_coin_qd function with the change argument.
4. The function all calls the greedy_coin_pnd function with the change argument.
"""


@main.command("all")
@click.argument("change", type=float)
def all(change):
    """
    Return the minimum number of coins for a given change
    using all coins
    example: ./new_greedy_coin_copilot 0.99
    """
    print("<-------------- All coins -------------->\n")
    greedy_coin(change)
    print("<-------------- Quarters and Dimes -------------->\n")
    greedy_coin_qd(change)
    print("<-------------- Pennies, Nickels and Dimes -------------->\n")
    greedy_coin_pnd(change)


# <------------------------------------------------------------------->
# <------------------------ Main Function ---------------------------->
# <------------------------------------------------------------------->
# build the main function
# explain the function in detail
"""
1. The if __name__ == "__main__": block calls the main function.
"""
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()


# clear
# virtualenv ~/.venv
# vim ~/.bashrc
# source ~/.venv/bin/activate
