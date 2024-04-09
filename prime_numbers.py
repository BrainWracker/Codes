import time


def findPrimes(num):

    if num <= 2:
        return []

    a = [2]

    for n in range(3, num, 2):
        isPrime = True
        for i in range(3, int(num**0.5)+1, 2):
            if n % i == 0:
                isPrime = False
                break
        if isPrime:
            a.append(n)

    return a


def sieve(num):

    if num <= 2:
        return []
    
    sie = [True] * num
    sie[0] = sie[1] = False
    
    primes = []

    for n in range(2, num):
        if sie[n] == False:
            continue;
        primes.append(n)
        for m in range(2*n, num, n):
            sie[m] = False

    return primes


if __name__ == '__main__':
    
    N = 10000

    start_time = time.time()
    primes = findPrimes(N)
    end_time = time.time()

    print('Функция findPrimes.')
    print('Найденные простые числа:', primes, 'Время (с):', end_time - start_time, sep='\n')
    print() # new line

    start_time = time.time()
    primes = sieve(N)
    end_time = time.time()

    print('Функция sieve.')
    print('Найденные простые числа:', primes, 'Время (с):', end_time - start_time, sep='\n')