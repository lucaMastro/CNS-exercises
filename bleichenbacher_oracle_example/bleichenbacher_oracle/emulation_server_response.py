import RSA_manager.rsa_manager as rsa_m
import bleichenbacher_oracle.binary_form_manager as bfm

def emulation_server(CT_1, private_key, N, size):
    PT_1 = rsa_m.encrypt(CT_1, private_key, N)
    binary = bfm.to_binary_form(PT_1, size)
    return binary[0]
