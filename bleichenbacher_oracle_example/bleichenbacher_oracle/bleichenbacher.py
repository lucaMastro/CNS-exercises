from math import ceil, log 
from time import sleep

#import RSA_manager.encryption as rsa_m 
import bleichenbacher_oracle.emulation_server_response as esr
import bleichenbacher_oracle.binary_form_manager as bfm


def stampa_range(r):
    for i in r:
        print(i, int(i, 2))
    print("\n")

def attack(public_key, private_key, N, CT):
    valid_range = [] # all number from 0 to N-1 in binary form
    count_iteration = 1
    size = ceil( log(N, 2) )
    all_value = []
    tmp = []
    
    for i in range(N):
        all_value.append(i)
        valid_range.append(i)
    
    print("\nThe number of possible values is: %d" %(N))
    while len(valid_range) > 1:
        print("\nIteration_numer %d:" %(count_iteration))
        print("Sending to oracle CT' = CT * (2^%d)^public_key"
                %(count_iteration))
        r = int(pow(2, count_iteration) )
        for i in all_value:
            tmp.append(bfm.to_binary_form(r * i % N, size))


        CT_1 = int( (pow(r, public_key) * CT) % N )

        print("The message CT' is: %d, " %(CT_1))
        print("Querying the oracle to know the first bit of PT'")

        # emulation oracle querying:
        # all the params passed should be known by server, except of course
        # for the CT_1
        # This line should be substited by the ones that trasmits the message
        bit_0 = esr.emulation_server(CT_1, private_key, N, size)
        print("First bit of PT' is " + bit_0)
        print("Reducing possible values...") 
     
        # deleting the values of valid_range that doesnt match the oracle 
        # response
        for i in range(len(tmp)):
            if tmp[i][0] != bit_0 and i in valid_range:
                valid_range.remove(i)
        print("There still are %d possibile values\n" %(len(valid_range)))

        # incresing the exponet and refresh tmp array
        count_iteration += 1
        tmp = []

    try:
        print("\nThe attack gives the output: %d\n" %(valid_range[0]))
    except:
        print("Something went wrong: the list of possible values is empty.")

