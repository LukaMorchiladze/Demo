Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# The sum of the primes below 10 is
# 2+3+5+7 = 17
#Find the sum of all the primes below two million.

# for n in range(39): print(n ** 2 + n + 41)


... def prime(x):
...     if (x == 2) or (x == 3): prm = True
...     else:
...         prm = False
...     while not(prm):
...         for i in range(2, x//2+1):
...             prm = True
...             if x % i == 0:
...                 x += 1
...                 prm = False
...                 break
...     return x
... 
... 
... def sumPrimes(y, prnt=False):
...     sum = 2+3
...     x = 5
...     ch = ''
...     if prnt: print(' 2 + 3 +', end='')
...     while x <= y:
...         md = x % 6
...         if md == 1 or md == 5:
...             x = prime(x)
...             if x <= y:
...                 sum += x
...                 if prnt: print(ch, x, end='')
...                 ch = ' +'
...         x += 2
...     if not(prnt): print('sum', end='')
...     print(' =', sum)
...     return sum
... 
... 
... if __name__ == '__main__':
...     print(prime(101))
... 
... # Checking
...     sum = sumPrimes(10, True)
...     sum = sumPrimes(141, True)
