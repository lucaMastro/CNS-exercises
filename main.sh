#!/bin/bash

export PYTHONPATH="`pwd`"
ROOT="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
echo "$ROOT_PATH = '$ROOT'" > config/path_config

operations_list="\n
1. Bleichenbacher oracle example\n
2. Common modulus attack on RSA\n
3. Set-up a Shamir or Trivial Secret Sharing scheme\n
4. Example of Secure Multiparty Computation\n
5. Example of Feldman or Pedersen Verifiable Secret Sharing Scheme\n
"

bleichenbacher(){
  python bleichenbacher_oracle/main.py
}
com_mod_att(){
  python common_modulus_attack/main.py 
}
secret_sharing(){
  python secret_sharing/main.py
}
sec_mult_comp(){
  python secure_multiparty_computation/main.py 
}
verifiable(){
  python verifiable_secret_sharing/main.py
}

invocation_function(){
  #$1 is the cmd obteined:
  if [ $1 -a $1 -eq 1 2>/dev/null ]; then
    bleichenbacher
  elif [ $1 -a $1 -eq 2 2>/dev/null ]; then
    com_mod_att
  elif [ $1 -a $1 -eq 3 2>/dev/null ]; then
    secret_sharing
  elif [ $1 -a $1 -eq 4 2>/dev/null ]; then
    sec_mult_comp
  elif [ $1 -a $1 -eq 5 2>/dev/null ]; then
   verifiable 
  else
    echo "error: invalid index"
  fi
}



clear
echo "Welcome in the starting point of exercises."
while true; do
  echo "What you should do is:"
  echo -e $operations_list
  echo -e "\nWhat do you want to exec?"
  read cmd
  invocation_function "$cmd"
  echo "Press a key to continue (the screen will be clean): "
  read
  clear
done
