#import sys
#sys.path.append("/home/luca/Scrivania/CNS/esercizi")

import secret_sharing.trivial_secret_sharing.trivial_secret_sharing_scheme as tss

def privacy_peer_function(modulus, secrets_shared):
    return tss.reconstruction(secrets_shared, modulus)

