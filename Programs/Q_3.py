# # Test the throughput performance of RSA, both encryption (using e) and decryption (using d), for following parameters:
# # n: 768 bits, e = 65537
# # n: 1024 bits, e = 5
#
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_OAEP
# import binascii
# import time
#
#
#
# def process(plainText, private_key, public_key):
#     start = time.time()
#     # ENC
#     encrypted = private_key.encrypt(plainText.encode('utf-8'), 32)
#     # DEC
#     private_key.decrypt(encrypted)
#     print('Executed RSA', time.time() - start, 'seconds')
#
#
#
# # -- Opening Message.txt to read text data stored in it --
#     # Below 3 lines import data in Message.txt and read it and saves data in plaintext
#
# with open('Message.txt', 'r', encoding='utf-8', errors='ignore') as file:
#     lines = file.readlines()
#     plainText = ''.join(lines)
#
# private_key = RSA.generate(1024, randfunc=None, e=65537)
# public_key = private_key.publickey()
# print(private_key)
# print(public_key)
#
# process(plainText,private_key,public_key)


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time


def encrypt(plaintext, public_key):
    rsa_cipher = PKCS1_OAEP.new(public_key)
    ciphertext = rsa_cipher.encrypt(plaintext.encode())
    return ciphertext


def decrypt(private_key):
    rsa_cipher = PKCS1_OAEP.new(private_key)
    decrypted_text = rsa_cipher.decrypt(ciphertext)

    return decrypted_text

# e = 65537
private_key1 = RSA.generate(2048, randfunc=None, e=65537)
public_key1 = private_key1.publickey()



plaintext = "Hii I am Piyush !"

for i in range(1,20):
    start = time.time()
    # calling encrypt func
    ciphertext = encrypt(plaintext, public_key1)
    # calling decrypt func
    decrypted_text = decrypt(private_key1)
# print decrypted plaintext
print(decrypted_text.decode())
print('Executed RSA when e = 65537, time taken:', time.time() - start, 'seconds')



# e = 5
private_key1 = RSA.generate(1024, randfunc=None, e=5)
public_key1 = private_key1.publickey()

for i in range(1,20):
    start = time.time()
    # calling encrypt func
    ciphertext = encrypt(plaintext, public_key1)
    # calling decrypt func
    decrypted_text = decrypt(private_key1)
# print decrypted plaintext
print(decrypted_text.decode())
print('Executed RSA when e = 5, time taken:', time.time() - start, 'seconds')