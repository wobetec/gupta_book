from math import sqrt
from os import system

#01 (recursive, iteration and recursive with cache)

#02
def fac(n):
    def is_prime(x):
        prime = True
        for i in range(2, int(sqrt(x))+1):
            if x % i == 0:
                prime = False
                break
        return prime
    
    primes = [x for x in range(2, int(sqrt(n))+1) if is_prime(x)]
    
    factors = []
    for prime in primes:
        count = 0
        while n % prime == 0:
            count += 1
            n = n/prime
        if count != 0:
            factors.append((prime, count))
        
    return factors

#03 simple condition question

#04 collatz sequence and use len in list

#05 it is possible to use complex() and add them

#06 already did that

#07 
def harshad(n):
    string = str(n)
    soma = sum([int(i) for i in string])
    return n % soma == 0

#08 could be done with simple list comprehention

#09 could use list.count() > 1

#10 
def f_10(n, tol = 0.0001):
    soma = 0
    term = 1
    while term > tol:
        soma += term
        term *= 1/n
    return soma

#11
def f_11(tol = 0.000001):
    soma = 0
    term = 1
    n = 1
    while abs(term) > tol:
        soma += term
        term *= (-(2*n-1)/(2*n+1))
        n += 1
    return soma*4

#12 simple, just a modifing the #11

#13 finantial math

#14 take a look at 6.14

#15 use brute force is a possibility

#16 run prime_finder with cache

#17 use a bin converter and the palindrome_checker

#18 save fib in a list and then use list comprehention

#19 just get the interval with range and run a simple prime_checker

#20
def f_20(lista):
    n, count = lista[0], lista.count(lista[0])
    conjunto = set(lista)
    for i in conjunto:
        this = lista.count(i)
        if this> count:
            n, count = i, this
    return n

#21 convert to set and use & operator

#22 use a for to append

#23 dont understand

#24
def f_23(string):
    char = string[0]
    max_char = char
    count = 1
    max_count = count
    for i in string[1:]:
        if i == char:
            count += 1
        else:
            if max_count < count:
                max_count = count
                max_char = char
            char = i
            count = 1
    if max_count < count:
        max_count = count
        max_char = char

    return max_char, max_count


#25 Transform into a list them use #24 to find de bigest sequence

#26 Collatz sequence

#27 Dont understand

#28
def f_28(n):
    tower = [list(range(n, 0, -1)), [], []]
    moves = 0

    def move(line_a, line_b):
        if len(tower[line_b]) == 0 or tower[line_b][-1] > tower[line_a][-1]:
            tower[line_b].append(tower[line_a].pop(-1))
            return True
        else:
            return False
    
    def show():
        print("################")
        for i in tower:
            print(i)
        print("################")

    def main():
        while True:
            system("cls")
            show()
            a, b = input("from / to: ").split()
            move(int(a), int(b))
    
    def main_alg():
        show()
        recursive(n, 0, 2)
        show()

    #A, B, C
    dic = {1:2, 2:1, 3:0}
    def recursive(n, begin, end):
        aux = dic[begin+end]
        if n != 1:
            recursive(n-1, begin, aux)
            move(begin, end)
            recursive(n-1, aux, end)
        else:
            move(begin, end)

    main_alg()


#29 - 40 this is a basic matrix problems, easy to implement


