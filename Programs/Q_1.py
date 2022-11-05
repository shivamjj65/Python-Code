# Implement the Extended Euclid Algorithm and output a, b and c = gcd(u,v) for the following inputs: u = 612898 and v = 765051

def findgcd(a,b):
    if a == 0:
        return b,0,1

    gcd,x,y = findgcd(b%a,a)
    m = y - (b//a)*x
    n = x
    return gcd,m,n


gcd,x,y = findgcd(612898,765051)
print("GCD of 612898 & 765051 is", gcd)
