#!/bin/bash

rm plot.txt
echo "Enter the secret key of 16 bytes:\n"
read secret_key
echo "Enter the message of 16 bytes:\n"
read message
echo ""

echo "Executing Noval Twofish Algorithm"
python noval_twofish.py $secret_key $message

echo ""
echo "Executing Twofish Algorithm"
python twofish_.py $secret_key $message

echo ""
echo "Executing 3DES Algorithm"
python 3des.py $secret_key $message

echo""
echo "\n\nExecuting RSA Algorithm\n\n"
python rsa.py $secret_key $message

echo "Ploting the graph"
python plot.py
