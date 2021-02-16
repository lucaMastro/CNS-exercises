#importing 'esercizi' folder
#import sys
#sys.path.append("/home/luca/Scrivania/CNS/esercizi")
import math_package.math_module as mm

def find_phi_coprime(phi, still_used_keys = None):
    # this function return a number which is coprime with phi
    coprime_value = 2
    while True:
        if (mm.mcd(coprime_value, phi) == 1):
            if (still_used_keys is None or 
                    coprime_value not in still_used_keys):
                break
            else:
                coprime_value += 1
        else:
            coprime_value += 1
    return coprime_value


def generate_keys(p, q, still_used_keys = None):
    N = p * q
    phi = (p - 1) * (q - 1)
    
    #print("Phi value %d" %(phi))

    # finding a number coprime with phi
    public_key = find_phi_coprime(phi, still_used_keys)
    #print("Public key found: %d" %(public_key))
    #print("Need to invert it...")
    #print("Computing:\tphi * a + public_key * b = 1")
    ret = mm.extended_euclidean_algorithm(phi, public_key)
    a = ret[0]
    b = ret[1]

    #print("Found (a, b): (%d, %d)" %(a, b) )
    if (b < 0):
    #    print("Computing a positive value for b mod %d" %(phi))
        while b < 0:
            b += phi

    #print("Private_key found: %d" %(b))
    
    ret[0] = public_key
    ret[1] = b
    return ret


def encrypt(value, key, module):
    try:
        return pow(value, key, module)

    except OverflowError:
        print("\nError detected: too large values\n")
        return -1

