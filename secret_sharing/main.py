#!/usr/bin/env python
#import sys
#sys.path.append('/home/luca/Scrivania/CNS/esercizi')

import math_package.math_module as mm


def print_divider():
    print("\n", end = "*" * 30 +"\n")



if __name__ == "__main__":
    print("Welcome in a dummy exemple of Shamir Secret Sharing Scheme.")
    print("First of all, give me the scheme (t,n). Please insert two values:")
    try:
        t = int(input("Give me t: "))
        n = int(input("Give me n: "))
    except:
        print("You didnt insert an integer.")
        exit(-1)
    
    trivial = False
    if t == n:
        print("I categorically refuse to use shamir scheme for (n,n) scheme. I will run trivial scheme.")
        trivial = True
    else:
        print("I'will realize a scheme (%d, %d)" %(t, n))



    print_divider()

    
