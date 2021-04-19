import itertools
import math
import time


# megaprime combinations for different digits
def candidates(k):
    # finds all candidate megaprimes with k digits
    for p in itertools.product(['2', '3', '5', '7'], repeat=k):
        yield int(''.join(p))


# check for prime
def isPrime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for k in range(3, 1 + int(1 + math.sqrt(n)), 2):
            if n % k == 0:
                return False
        return True


def findMegaPrimes(n):
    # finds all megaprime numbers < 10**n
    megasPrimes = []
    for k in range(1, n + 1):
        for c in candidates(k):
            if isPrime(c):
                megasPrimes.append(c)
    return megasPrimes


# print results
tic = time.perf_counter()
mp = findMegaPrimes(9)  # for 10**9 (1 billion)
toc = time.perf_counter()
print(len(mp))  # result: 23169
print(mp)
print(toc - tic)  # result: 23.832374017 secs
