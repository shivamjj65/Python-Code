# I have imported all required libraries here
import os
import time
from Crypto import Random
from Crypto.PublicKey import RSA

key = RSA.generate(768,randfunc=None,e=65537)
