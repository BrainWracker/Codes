import time
def findPrimes(num):
    a = [2] if num > 2 else []
    for n in range(3, num, 2):
        flag = 1
        for i in range(3, n//2+1, 2):
            if n%i == 0:
                flag = 0
                break
        if flag:
            a.append(n)
    return a

def sieve(num):
    a = list(range(2, num))
    for x in range(2, int(num**0.5)+1):
        for y in range(2*x, num, x):
            if y in a:
                a.remove(y)
    return a

start_time = time.time()
print(findPrimes(100), time.time() - start_time)
start_time = time.time()
print(sieve(100), time.time() - start_time)
