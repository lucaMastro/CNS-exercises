#!/usr/bin/env python
#import multiprocessing as mp
import random as r
import time as t
import sys
sys.path.append('/home/luca/Scrivania/CNS/esercizi')

import math_package.math_module as mm
import input_peer as ip
import privacy_peer as pp

welcome_msg = """Welcome to dummy example of secure_multiparty_computation.
First of all, tell me how many input peers you want simulate:"""

execution_msg = """
Each peer will generate a (2, 2) secret sharing scheme and
will share secrets among 2 privacy peers. Let's start."""

end_msg ="""
privacy_peer1 reconstruction's: %d
privacy_peer2 reconstruction's: %d
their modular sum: %d

is it equal to the modular sum of input_peer secrets? 
This value is: %d

"""

def print_divider():
    print("\n", end = "*" * 30 +"\n")

if __name__ == "__main__":
    if sys.argv[1] != "":
        mm.MAX_INT_VALUE = int(sys.argv[1])
    print(welcome_msg) 
    try:
       peers = int(input("input peers: "))
    except:
        print("Not int value inserted. exiting")
        exit(-1)

    print(execution_msg)
    print_divider()
    print() 
    r.seed(t.time)
    
    print("generating random secrets, one for each input_peer: ")
    secrets = []
    for i in range(peers):
        secrets.append(r.randint(2, mm.MAX_INT_VALUE))
    print(secrets, "\n")

    print("generating random modulus: ", end="")
    modulus = r.randint(2, mm.MAX_INT_VALUE)
    print(modulus, "\n")

    print("simulating input_peers behaviour")
    shares = []
    for i in range(peers):
        curr = ip.input_peer_function(secrets[i], modulus)
        shares.append(curr)
        print("input_peer_%d_shares:" %(i + 1))
        print(curr)
    
    print()    
    print("Each input peer send a share to each privacy peer")

    privacy_peers_input = []
    for i in range(2):
        curr = []
        for j in range(peers):
            curr.append(shares[j][i])
        privacy_peers_input.append(curr)

    print("privacy peer 1 receives: ", end="")    
    print(privacy_peers_input[0])
    print("privacy peer 2 receives: ", end="")    
    print(privacy_peers_input[1])
    print()

    
    secrets_reconstruction = []
    for i in range(2):
        rec = pp.privacy_peer_function(modulus, privacy_peers_input[i])
        secrets_reconstruction.append(rec)

    reconstructed_modular_sum = (secrets_reconstruction[0]
            + secrets_reconstruction[1]) % modulus

    truly_secret_sum = 0
    for s in secrets:
        truly_secret_sum += s % modulus
    truly_secret_sum = truly_secret_sum % modulus

    print(end_msg %(secrets_reconstruction[0], 
        secrets_reconstruction[1], 
        reconstructed_modular_sum,
        truly_secret_sum
        ))

    
       


