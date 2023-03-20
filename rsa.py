import math
import time


from qiskit import QuantumCircuit, execute, Aer
from qiskit.compiler import transpile, assemble

from qiskit.tools.visualization import plot_histogram
from qiskit.visualization import *
from qiskit.aqua.algorithms import Shor
from qiskit.aqua import QuantumInstance
import numpy as np
import pandas as pd
from fractions import Fraction


def letterToNumber(letter):
    return ord(letter) - 96

def numberToLetter(number):
    return chr(number + 96)

def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1


def mymod(a,b):
    m = a % b
    f = a // b
    return m

def finde(N,phi):

    for x in range(2,phi):
        #print("Checking if " + str(x) + " is a coprime with " + str(phi) + " = " + str(is_coprime(phi,x)))
        if is_coprime(phi,x):
            return x
    return False

def isPrime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def findd(e,phi):
    loop = True
    x = e
    counter = 1
    while ( loop ):
        #print("Check number " + str(counter) + ". What does " + str(x) + " = mod(" + str(phi) + ") = " + str(mymod(x,phi))  )
        if mymod(x,phi) == 1: return counter

        x = x + e
        counter = counter + 1
        #you would normally pick a later numvber that equals 1 not the first
    return False





print("RSA - Rivest, Shamir, Adleman - Cryptography break down")
print()



print("****************Key Creation*******************")

p = 3 
q = 7
N = p * q
print("You picked two prime numbers, which are p = " + str(p) + " and q = " + str(q) + " the product of q and q is N/" + str(N))
phi = (p -1) * (q -1)#number of coprime = Euler Totient
print("The phi function of N = " + str(phi))




print("Next we need a encryption number that is bigger than 1, less than " + str(phi) + " and must be co-primed with N/" + str(N) + " and phi/" + str(phi))
e = finde(N,phi)
print("My encryption key is (" + str(e) + "," + str(N) + ") This is my Public key, anyone can use this to encypt messages for me")
print()


print("Now we need a decryption number d that: d * e mod(phi) = 1")
d = findd(e,phi)
print("My decryption key is (" + str(d) + "," + str(N) + ") This is my Private key only I have this to decrypot my messages")
print()











print()



print("****************Encryption*******************")
m = "f" #message to encryot
numberm = letterToNumber(m)#convert to number

print("Message to encypt = " + m + ", " + m + " as a number = " + str(numberm))




print("The encryption key is (" + str(e) + "," + str(N) + ")")

enc3 = numberm ** e
print(str(e) + " to the power of " + str(numberm) + " = " + str(enc3))


cipherTextNumber = mymod(enc3,N)
cipherText = numberToLetter(cipherTextNumber)
print(str(enc3) + " (mod " + str(N) + ") = " + str(cipherTextNumber))

print()
print("The Ciphertext = " + cipherText  + " which equals the number " + str(cipherTextNumber))
print()




print("****************Decryption*******************")

#dec1 = 11

print("The decryption key is (" + str(d) + "," + str(N) + ")")

dec3 = cipherTextNumber ** d
print(str(d) + " to the power of " + str(cipherTextNumber) + " = " + str(       len(str(dec3))          ) + " digits long")

deCipherTextNumber = mymod(dec3,N)
deCipherText = numberToLetter(deCipherTextNumber)
#print(str(dec3) + " (mod " + str(N) + ") = " + str(deCipherTextNumber))


print()
print("The Deciphererdtext = " + deCipherText  + " which equals the number " + str(deCipherTextNumber))
print()





print()
print("****************Can I brute force this message*******************")
print()
print("I know N from the public key, N = " + str(N))
print("I know e from the public key, e = " + str(e))
print("I know the cipher text " + cipherText + "/" + str(cipherTextNumber))
print()
print("Lets list all the primes that multiplied together = N/" + str(N))

a = 0
b = 0
start = time.time()
for x in range(2,N):
    if N % x == 0:
        if isPrime(x):
            if a == 0: 
                a = x
            else:
                b = x
              
            print(str(x) + " is a factor of N/" + str(N) + " and is a prime")
end = time.time()

print("finding the factors " + str(a) + " and " + str(b) + " of " + str(N) + " took " + str(end-start) + " seconds to find")
hackedP = a
hackedQ = b
hackedPhi = (hackedP -1) * (hackedQ -1)


hackedE = finde(N,hackedPhi)
hackedD = findd(hackedE,hackedPhi)


hackedDec3 = cipherTextNumber ** hackedD

hackedDeCipherTextNumber = mymod(hackedDec3,N)
hackedDeCipherText = numberToLetter(hackedDeCipherTextNumber)


print()
print("The hacked deciphererd text = " + hackedDeCipherText  + " which equals the number " + str(hackedDeCipherTextNumber))
print()





print("****************Can I find p and q using shors algorithm on a quantum computer*******************")
print()
print("I know N from the public key, N = " + str(N))
print("I know e from the public key, e = " + str(e))
print("I know the cipher text " + cipherText + "/" + str(cipherTextNumber))
print()
p


backend = Aer.get_backend('qasm_simulator')
quantum_instance = QuantumInstance(backend, shots=1000)

my_shor=Shor(N=N,a=2,quantum_instance=quantum_instance)

output = Shor.run(my_shor)

quantumPrimes = output["factors"]

print("The factors are " + str(quantumPrimes[0][0]) + " and " + str(quantumPrimes[0][1]))

qP = quantumPrimes[0][0]
qQ = quantumPrimes[0][1]
qPhi = (qP -1) * (qQ -1)

qE = finde(N,qPhi)
qD = findd(qE,qPhi)

qDec3 = cipherTextNumber ** qD

qDeCipherTextNumber = mymod(qDec3,N)
qDeCipherText = numberToLetter(qDeCipherTextNumber)


print()
print("The deciphererd text using a quantum computer = " + qDeCipherText  + " which equals the number " + str(qDeCipherTextNumber))
print()


