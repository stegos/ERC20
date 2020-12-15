#!/usr/bin/python3

from brownie import Token, accounts

def main():
    acct = accounts.load('test')
    return Token.deploy("Stegos", "STG", 6, 1e15, {'from': acct})
