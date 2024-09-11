import random as r
from math import sqrt

MAX_INT_VALUE = pow(2,64)


def mcd(a, b):
    r = a % b
    while r > 0:
        a = b
        b = r
        r = a % b
    return b


def extended_euclidean_algorithm(first_line_val, second_line_val):
    """   
    i'll check for the sign of values in order to manage negative numbers, 
    using:
    a * x + b * y = 1
    then, if x and y are negative, it can be write as:
    (a * sign(x)) * |x| + (b * sign(y)) * |y| = 1
    """
    a_sign = 1
    b_sign = 1
    if (first_line_val < 0):
        a_sign = -1
        first_line_val = abs(first_line_val)
    if (second_line_val < 0):
        b_sign = -1
        second_line_val = abs(second_line_val)
    
    """
    val is initialized to second_line_val because it could be 1 or -1.
    In that case, it should simply terminate without entering in while loop
    """
    val = second_line_val
    rem = 0
    first_line_a = 1
    first_line_b = 0
    second_line_a = 0
    second_line_b = 1
   # third_line_a = 1
   # third_line_b = 0
    """ 
    third_line_a and third_line_b are initialized to second_line_a and
    second_line_b because if the second_line_val == 1 or -1, the output of
    extended_euclidean_algorithm is simply the second line
    """
    third_line_a = second_line_a
    third_line_b = second_line_b

    return_values = []

    while val != 1:
        rem = int(first_line_val / second_line_val)
        val = first_line_val % second_line_val

        third_line_a = first_line_a - (second_line_a * rem)
        third_line_b = first_line_b - (second_line_b * rem)

        # swapping values:
        first_line_a = second_line_a
        first_line_b = second_line_b

        second_line_a = third_line_a
        second_line_b = third_line_b

        first_line_val = second_line_val
        second_line_val = val

    return_values.append(third_line_a * a_sign)
    return_values.append(third_line_b * b_sign)
    #return_values[0] = (third_line_a * a_sign)
    #return_values[1] = (third_line_b * b_sign)
    return return_values


def lagrange_coefficient(list_, modulus):
    #output of this function is a list of lagrange coefficients
    #evaluated in 0

    l = len(list_) #i dont know how many xi used
    ret = []

    #print(list_)
    for i in range(l):
        xi = list_[i]
        li = 1
        for j in range(l):
 #           print(i, j)
            
            if j == i:
                continue

            xj = list_[j]
            #need to calculate (xi - xj)^(-1)
            to_inverte = xi - xj
            inverse = extended_euclidean_algorithm(modulus, to_inverte)[1]\
                    % modulus
           
            li *= (-xj * inverse) 
        ret.append(li)

    for i in range(len(ret)):
        ret[i] = ret[i] % modulus
    return ret



def is_prime(n):

    if type(n) != int:
        print("error")
        return


    is_prime = True
    square_t = int(sqrt(n))
    
    for i in range(2, square_t + 1):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


def find_nth_prime(n):
    # start from 3, setting step=2: so that i can exclude all even numbers in
    # while
    if n == 1:
        return 2
    primes_found = 1
    current = 1
    while (primes_found != n):
        current += 2
        if is_prime(current):
            primes_found += 1
    return current


def make_random_polynom(grade, modulus = MAX_INT_VALUE):
    """
    this function will return a list with coefficients, ordered 
    by the less grade term to the highest one. For exemple, calling
    this function with grade=3, may return:
        [1, 2, 0, 2]
    means:
        1 + 2x + 2x^3

    the parameter modulus needs to set a threshold for random calls
    """
    coefficients = []
    for i in range(grade + 1):
        coefficients.append(r.randint(0, modulus - 1))

    return coefficients

def evaluate(polynom, x):
    """
    this function calculate the yi = (polynom_evaluate_in_x)
    exemple:
        evaluate([1, 0, 1 ], 2) 
    means we want to know y = 1 + x^2 when x = 2. Then the function
    returns 5
    """
    evaluation = 0
    for i in range(len(polynom)):
        if polynom[i] == 0:
            continue

        x_pow = pow(x, i)
        evaluation += x_pow * polynom[i]

    return evaluation


def find_nth_strong_prime(n):
    # p = 2q + 1
    count = 0
    q = p = 1
    while True:
        p = 2 * q + 1
        if is_prime(q) and is_prime(p):
            count += 1
        if count == n:
            break
        q += 1
    return p
