import random as r
import time 

import secret_sharing.shamir_scheme.shamir_secret_sharing_scheme as ss
import math_package.math_module as m

def find_random_strong_prime():
    r.seed(time.time)
    n = r.randint(1, 500)
    p = m.find_nth_strong_prime(n)
    return p

def generate_random_polynom(t, q):
    return m.make_random_polynom(t, q)

def generates_commitments(polynom, gen, p):
    #generate commitments:
    commitments = []
    l = len(polynom)
    for i in range(l):
        commitments.append(pow(gen, polynom[i], p))
    
    return commitments

def generate_shares(polynom, n, q):
    shares = ss.generate_shares(polynom, n, q)
    return shares

def reconstruction(shares, q):
    return ss.reconstruction(shares, q)

def is_quadratic_residue(g, p):
    #   legendre_symbol == 1 means:
    #   g^0%p=1, .... , )g^(q-1)) % p, (g^q) % p == g^0%p == 1. 
    #   then the order of subgroup is q
    #
    q = (p - 1) / 2
    q = int(q)
    legendre_symbol = pow(g, q, p)
    return legendre_symbol == 1


def evaluate_commitments(commitments, xi, p):
    #   computing:
    #    
    #    l           j                      2
    #   ____    (xi)             xi       xi
    #    ||   Cj        = C0 * C1   *  C2
    #   j=0
    #
    #   l == len(commitments) - 1

    
    #computing xi's pow
    pows = []
    for i in range(len(commitments)):
        pows.append(pow(xi, i))

    product = 1
    for i in range(len(commitments)):
        product *= pow(commitments[i], pows[i], p)

    return product % p



def check_commitments(gen, commitments, disclosed_value, p, xi):
    #(t, n) scheme => len(shares) >= len(commitments):
    #in fact: len(commitments) == t
    #         len(shares) == n
    
    #checking if gen is quadratic residue
    if not is_quadratic_residue(gen, p):
        print("g offered is not a quadratic residue")
        exit(-1)

    computed_value = evaluate_commitments(commitments, xi, p)
    
    return computed_value == disclosed_value


def compute_value_to_disclose(g, yi, p):
    return pow(g, int(yi), p)

    

if __name__ == '__main__':
    import sys
    sys.path.append("/home/luca/Scrivania/CNS/esercizi")
    
    #finding nth strong_prime
    r.seed(time.time)
    n = r.randint(1, 500)
    p = m.find_nth_strong_prime(n)
    q = (p - 1)/2

    t = 3
    n = 5
    polynom = generate_random_polynom(t, q)
    shares = generate_shares(polynom, n, q)
    s = reconstruction(shares, q)
    print("secret = ", s)
    print(s == polynom[0])

    g = r.randint(1, p - 1)
    gen = pow(g, 2, p)
    print(g, is_quadratic_residue(g, p))
    print(gen, is_quadratic_residue(gen, p))

    commitments = generates_commitments(polynom, gen, p)
    for i in shares:
        yi = i[1]
        xi = i[0]
        disclose = compute_value_to_disclose(gen, yi, p)
        check_commitments(gen, commitments, disclose, p, xi)



