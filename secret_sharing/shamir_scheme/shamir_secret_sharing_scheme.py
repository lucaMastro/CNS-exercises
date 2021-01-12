import random as r
import sys
sys.path.append("/home/luca/Scrivania/CNS/esercizi/")

import math_package.math_module as m

def generate_random_polynom(t, modulus):
    return m.make_random_polynom(t - 1, modulus)


def generate_shares(polynom, n, modulus):
    shares = []
    for i in range(n):
        #x = r.randint(1, m.MAX_INT_VALUE)
        #conviene usare xi = i
        x = i + 1 #starting from 1
        y = m.evaluate(polynom, x) % modulus

        shares.append([x,y])

    return shares
    

def reconstruction(shares, modulus):
    l = len(shares)

    xi_list = []
    for i in range(l):
        xi_list.append(shares[i][0])

    l_coeff = m.lagrange_coefficient(xi_list, modulus)
    
    print(l_coeff)
    evaluation = 0
    for i in range(l):
        evaluation += (l_coeff[i] * shares[i][1]) % modulus

    return evaluation % modulus


if __name__ == '__main__':
    modulus = m.find_nth_prime(r.randint(2, 100))
    print("using %d as modules" %(modulus))
    s = r.randint(2, 10)
    print("using %d as secret" %(s))

    print("implementing (t,n) = (3,4)")
    t, n = 3, 4
    #generating a random polynom
    polynom = generate_random_polynom(t, modulus)
    polynom[0] = s
    print("polynom = ", polynom)

    #genereting n shares:
    shares = generate_shares(polynom, n, modulus)
    print(shares)

    shares = shares[:-1]
    print(shares)

    #recostruction:
    s_ = reconstruction(shares, modulus)
    print(s_)



