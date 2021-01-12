import random as r
import time as t

def generate_shares(secret, modulus, number_of_shares):
    #modulus is the modulus of shares and secrets
    r.seed(t.time())
    shares = []
    summ = 0
    for i in range(number_of_shares - 1):
        curr = r.randint(1, modulus - 1) % modulus
        shares.append(curr)
        summ += curr
        
    shares.append((secret - summ) % modulus)
    return shares   


def reconstruction(list_of_shares, modulus):
    l = len(list_of_shares)
    sum_ = 0
    for i in range(l):
        sum_ += list_of_shares[i] % modulus

    return sum_ % modulus



