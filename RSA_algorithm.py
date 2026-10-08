from Crypto.Util.number import inverse, getPrime
import math

bit_length = 1024
m = int(input("Enter value of m: "))

while True:
    p:int=getPrime(bit_length)
    q:int=getPrime(bit_length)
    n:int = p*q
    phi:int = (p-1)*(q-1)
    e:int = 65537 

    if math.gcd(e, phi) == 1:
        break

d:int = inverse(e,phi)
public_key:tuple = (n,e)
private_key:tuple = (n,d)

c = pow(m, public_key[1], public_key[0])
message = pow(c , private_key[1], private_key[0])

print("~~Your public Key and Private Key are in tuple form. (n,e) and (n,d)~~")
print("\n")
print("value of d :", private_key[1])
print("\n")
print("Cypher: ", c)
print("\n")
print("Decrypted : ", message)
print("\n")
print("---Your Public Key---")
print(public_key)
print("---Your Private Key---")
print(private_key)