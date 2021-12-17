from math import pi, sqrt, cos, log
from time import perf_counter
from random import randint

#6.1
def volume_of_a_sphere(radius):
    V = (4 * pi * radius**3)/3
    return V


#6.2
def heron_triangle_area_01(a, b, c):
    s = (a + b + c)/2
    A_2 = s * (s-a) * (s-b) * (s-c)
    return sqrt(A_2)

def heron_triangle_area_02(a, b, theta):
    theta_rad = pi * theta / 180
    c = sqrt(a**2 + b**2 - 2 * a * b * cos(theta_rad))
    s = (a + b + c)/2
    A = sqrt(s * (s-a) * (s-b) * (s-c))
    return A


#6.3
def odd_or_even(n):
    if n%2 == 0:
        return "Even"
    else:
        return "Odd"

def odd_or_even_list(lista, even=True):
    if even:
        f = lambda x: True if x % 2 == 0 else False 
    else:
        f = lambda x: False if x % 2 == 0 else True

    new_lista = list(filter(f, lista))
    return new_lista


#6.4
def factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return factorial_recursive(n-1) * n

def factorial_iterative(n):
    fac = 1
    for i in range(2, n+1):
        fac *= i
    return fac


#6.5
def ln_stirling(n):
    ln = n *log(n) - n
    return ln


#6.6 primes
def prime_primitive(n):
    prime = True
    for i in range(2, n):
        if n%i ==0:
            prime = False
            break
    return prime

def prime_2(n):
    prime = True
    for i in range(2, int(sqrt(n))+1):
        if n%i ==0:
            prime = False
            break
    return prime

#6.7 perfect square numbers
def perf_square(n):
    raiz = sqrt(n)
    if int(raiz)**2 == n:
        return True
    else:
        return False


#6.8 Amstrong numbers
def armstrong(n):
    soma = sum([eval(i)**3 for i in str(n)])
    return soma == n


#6.9 Strong numbers
def strong_number(n):
    fac = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    soma = sum([fac[eval(i)] for i in str(n)])
    return soma == n

#6.10 Palindrome
def palindrome(string):
    reverse = string[::-1]
    return reverse == string


#6.11 Max e min
def maximum(lista):
    m = lista[0]
    for i in lista:
        if i>m: m = i
    return m

def minimum(lista):
    m = lista[0]
    for i in lista:
        if i<m: m = i
    return m


if __name__ == "__main__":

    pass
    





