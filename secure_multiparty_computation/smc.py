import time
import random
import sys
sys.path.append("/home/luca/Scrivania/CNS/esercizi")

import math_package.math_module as mm

def authority_server_function(modulus, secrets_shared):
    #modulus is used to calculate secret
    #secrets_shared is the list of shares
    sum_ = 0
    for i in range(len(secrets_shared)):
        sum += secrets_shared[i] % modulus
    return sum_


