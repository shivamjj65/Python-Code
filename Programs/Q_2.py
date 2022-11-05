# Estimate how many 768-bit prime numbers are there? & Generate 10 distinct 768-bit prime numbers and measure their generation time.

import math
from Crypto.Util import number

EstimatedBits = 768;
a = 2;
b = EstimatedBits-1;

x = math.pow( a, EstimatedBits) / math.log( math.pow( a, EstimatedBits) )
y = math.pow( a, b) / math.log( math.pow( a, b) )

ans = x - y

print ('768 bit long prime numbers are :', ans)

print("\nThe 10 unique 768-bit prime no's are:")
for i in range(1, 11):
    pn = number.getPrime(768)
    print("Number",i,":",pn)