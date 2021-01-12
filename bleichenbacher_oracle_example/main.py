#!/usr/bin/env python

import time
import random
import math
import sys
sys.path.append("/home/luca/Scrivania/CNS/esercizi")

import math_package.math_module as mm
import RSA_manager.rsa_manager as rsa_m
import bleichenbacher_oracle.bleichenbacher as boa 

MAX_PRIME_SIZE = 100

def print_divider():
    print("")
    for i in range(50):
        print("*", end = "") 
    print("\n") 

if __name__ == "__main__":
    print("Dummy example of Bleichenbacher's Oracle") 
    print_divider() 
    random.seed(time.time()) 
    print("Generating p and q primes.\nLet's start compute them betwen 1-st and %d-th" %(MAX_PRIME_SIZE)) 

    n = random.randint(1, MAX_PRIME_SIZE)
    p = mm.find_nth_prime(n) 
    q = p
    while q == p: 
        n = random.randint(1, MAX_PRIME_SIZE)
        q = mm.find_nth_prime(n) 

    N = p * q
    print("Primes:\np = %d\nq = %d" %(p, q)) 
    print("N = p * q = %d" %(N))
    print_divider()

    print("Need to find a public and private key pair: just computing it...\n")
    ret = rsa_m.generate_keys(p, q)
    public_key = ret[0]
    private_key = ret[1]
    print_divider()

    print("Let's try encryption and decryption.\nI will crypt a random value betwen 2 and %d:\t" %(MAX_PRIME_SIZE), end = "" ) 

    PT = random.randint(2, MAX_PRIME_SIZE)
    print("%d" %(PT))

    CT = rsa_m.encrypt(PT, public_key, N)
    if CT == -1:
        exit()
    print("Encrypted with public_key: %d" %(CT))

    decrypted = rsa_m.encrypt(CT, private_key, N)

    if decrypted == -1:
        exit()

    print("Decrypted with private_key: %d" %(decrypted))
    print_divider()

    print("Starting (semplified) Bleichenbacher's Oracle Attack")
    print("The attacker knows:")
    print("\tPublic_key: %d\n\tModulus N: %d\n\tCipher text: %d" 
            %(public_key, N, CT))

    attack_result = boa.attack(public_key, private_key, N, CT)
