#!/usr/bin/env python

import time
import random

import math_package.math_module as mm
import RSA_manager.rsa_manager as rsa_m

MAX_PRIME_SIZE = 100

def print_divider():
    print("")
    print("*" * 50)
    print("\n") 

if __name__ == "__main__":
    print("Dummy example of RSA Common Modulus Attack") 
    random.seed(time.time()) 
    print("Generating 2 RSA key pair...") 

    #finding 2 primes p and q:
    n = random.randint(1, MAX_PRIME_SIZE)
    p = mm.find_nth_prime(n) 
    q = p
    while q == p: 
        n = random.randint(1, MAX_PRIME_SIZE)
        q = mm.find_nth_prime(n) 
    N = p * q
    #phi = (p -1) *(q- 1)
    print("p = %d, q = %d" %(p, q))
    
    #generating 2 pair RSA with same modulus

    ret1 = rsa_m.generate_keys(p, q)
    
    #i want the pairs are differents
    #ret2 = ret1
    #while ret2 == ret1:
    ret2 = rsa_m.generate_keys(p, q, [ret1[0]])

    public_key1 = ret1[0]
    private_key1 = ret1[1]

    public_key2 = ret2[0]
    private_key2 = ret2[1]

    print("""RSA keys generated.
            First pair:
            \tPublic_key: (e, N) = (%d, %d)
            \tPrivate_key: d = %d
            Second pair:
            \tPublic_key: (e, N) = (%d, %d)
            \tPrivate_key: d = %d
            """ %(public_key1, N, private_key1, 
                public_key2, N, private_key2)
            )

    print("Trying attack on PT: ", end="")
    PT = random.randint(2, MAX_PRIME_SIZE)
    print("%d" %(PT))

    print_divider()


    CT1 = rsa_m.encrypt(PT, public_key1, N)
    if CT1 == -1:
        exit()
    CT2 = rsa_m.encrypt(PT, public_key2, N)
    if CT2 == -1:
        exit()
    print("Encrypted with private_key1: %d" %(CT1))
    print("Encrypted with private_key2: %d\n" %(CT2))

    s = "Starting Common Modulus Attack"
    print(s)
    print("_" * len(s))
    print("""
The attacker knows:
    public_key1: (e1, N) = (%d, %d) 
    CT1 = %d

    public_key1: (e2, N) = (%d, %d) 
    CT2 = %d
    """ %(public_key1, N, CT1,
                public_key2, N, CT2))
    
    print("""The attack can be done only if e1 and e2 are coprime.
Let's check it.""")

    if (mm.mcd(public_key1, public_key2) != 1):
        print("e1 and e2 are not coprime. Cannot continue..")
        exit(-1)

    print("e1 and e2 are coprimes!! The attack can be done")
    print("""
Looking for s ad r such that:
    s * e1 + r * e2 = 1
    """)

    ret = mm.extended_euclidean_algorithm(public_key1, public_key2)
    s = ret[0] 
    r = ret[1]
    print("s and r found: (s, r) = (%d, %d)" %(s, r))
    print("""
What to do now is:
    (CT1)^r = [(PT)^e1]^r = (PT)^(e1*r)
    (CT2)^s = [(PT)^e2]^s = (PT)^(e2*s)
and then multiplay them.
""")
    
    first = pow(CT1, abs(s), N)
    if s < 0:
        ret = mm.extended_euclidean_algorithm(N, first)
        first = ret[1]

    second = pow(CT2, abs(r) , N)
    if r < 0:
        ret = mm.extended_euclidean_algorithm(N, second)
        second = ret[1]


    res = first * second
    res = res % N
    print("The result is: %d" %(res))
        




