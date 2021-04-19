import time

num_limit = input("Enter maximum limit to find megaprimes from 1 to max: ")
max_val = int(num_limit)

# initiate prime list
primes = [2]
if max_val < 2:
    primes = []

# find prime numbers
divisors = [2]  # initiate divisor array
tic = time.perf_counter()
for i in range(3, max_val+1, 2):
    prime_flag = True
    for j in divisors:
        if i % j == 0:
            prime_flag = False
            break
    # if prime_flag & j > i:
    #     sqroot = i ** 0.5  # square root
    #     if sqroot % 1 > 0:
    #         primes.append(i)
    #         divisors.append(abs(sqroot))  # add to the divisor list
    if prime_flag:
        primes.append(i)
        divisors = primes

# print results
toc = time.perf_counter()
primeTime = toc-tic
print("Prime length:", len(primes))
print("Time taken:", primeTime)


# filter megaprime numbers from prime
megaPrimes = []
tic = time.perf_counter()
for number in primes:
    if '0' in str(number):
        continue
    if '1' in str(number):
        continue
    elif '4' in str(number):
        continue
    elif '6' in str(number):
        continue
    elif '8' in str(number):
        continue
    elif '9' in str(number):
        continue
    else:
        megaPrimes.append(number)

# print results
toc = time.perf_counter()
megaprimeTime = toc-tic
print("Megaprimes:", megaPrimes)
print("MegaPrime length:", len(megaPrimes))
print("Time taken:", megaprimeTime)
