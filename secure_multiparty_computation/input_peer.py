#import sys
#sys.path.append("/home/luca/Scrivania/CNS/esercizi")

import secret_sharing.trivial_secret_sharing.trivial_secret_sharing_scheme as tsh

#just implementing a trivial secret share (2,2). 
def input_peer_function(secret, modulus):
    return tsh.generate_shares(secret, modulus, 2)

