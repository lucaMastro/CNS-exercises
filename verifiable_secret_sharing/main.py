#!/usr/bin/env python
import time 
import random as r

import math_package.math_module as m
import feldman.feldman as m
#import pedersen.pedersen as p


if __name__ == '__main__':
    print("Welcome in simple Proof of Concept for Shamir Secret Feldamn/Pedersen verifiable secret sharing.")
    print("Sorry: not yet completed.")
    exit(0)
    
    print("First of all, give me the scheme (t,n). Please insert two values:")
    
    try:
        t = int(input("Give me t: "))
        n = int(input("Give me n: "))
    except:
        print("You didnt insert an integer.")
        exit(-1)
    
    print("Which schema would you to execute?\n\t1. Feldman\n\t2. Pedersen")
    try:
        schema_num = int(input(">  "))
    except:
        print("You didnt insert a valid integer.")
        exit(-1)

    if schema_num == 1:
        print("Running Feldman scheme...")
        
    elif schema_num == 2:
        print("Sorry: Pedersen scheme not yet implemented")
    
    else:
        print("You didnt chose a valid option.")

    print_divider()
