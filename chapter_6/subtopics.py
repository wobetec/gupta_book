from math import pi, sqrt, cos, log, factorial, modf
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

#6.12 Sorting list
def bubble_sort(lista):
    L = lista.copy()
    n = len(lista)
    np = 1
    while np:
        np = 0
        for i in range(1, n):
            if L[i] < L[i-1]:
                L[i], L[i-1] = L[i-1], L[i]
                np = 1
    return L


def insertion_sort(lista):
    L = lista.copy()
    n = len(L)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if L[j] < L[j-1]:
                L[j], L[j-1] = L[j-1], L[j]
            else:
                break

    return L


#6.13 Roots of quadratic equations
def quadratic_equation(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
    elif d < 0:
        x1 = complex(-b, sqrt(abs(d)))/(2*a)
        x2 = complex(-b, -sqrt(abs(d)))/(2*a)
    else:
        x1 = x2 = -b/(2*a)

    return x1, x2


#6.14 Mean, variance, standard deviation
def mean(lista):
    n = len(lista)
    mean1 = sum(lista)/n
    return mean1


def variance(lista):
    n = len(lista)
    square_mean = sum([i**2 for i in lista])/n
    mean_square = mean(lista)**2
    variance = square_mean - mean_square
    return variance


def standarf_deviation(lista):
    stdev = sqrt(variance(lista))
    return stdev


#6.15 Correlation coefficient
def variance_set(lista):
    mean1 = mean(lista)
    variance = sum([(i-mean1)**2 for i in lista])/len(lista)
    return sqrt(variance)

def covariance_set(lista1, lista2):
    mean1 = mean(lista1)
    mean2 = mean(lista2)
    covariance = sum([(i-mean1)*(j-mean2) for i, j in zip(lista1, lista2)])/len(lista1)
    return covariance


def correlation_coefficient(lista1, lista2):
    sigx = variance_set(lista1)
    sigy = variance_set(lista2)
    r = covariance_set(lista1, lista2)/(variance_set(lista1)*variance_set(lista2))
    return r


#6.16 Infinite Series
def taylor_exp(x, tol):
    soma = 0
    term = 1
    n = 1
    while abs(term) > tol:
        soma += term
        term = term * (x/n)
        n += 1
    
    return soma

def taylor_cos(x, tol):
    theta = pi * (x/180)
    soma = 0
    term = 1
    n = 1
    while abs(term) > tol:
        soma += term
        term *= (-theta**2/(2*n*(2*n-1)))
        n += 1
    return soma


def taylor_exp_list_comprehension(x, terms):
    lista = [x**i / factorial(i) for i in range(terms)]
    return sum(lista)


#6.17 Digits of a number


#6.18 check leap year
def check_leap_year(year):
    if year % 100 != 0 and year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


#6.19 Collatz Sequence
def collatz_sequence(n):
    lista = [n]
    while n > 1:
        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
        lista.append(int(n))
    return lista


#6.20 GCD and LCM (mdc e mmc)
def gcd_lcm(x, y):
    a = x
    b = y

    while a%b != 0 :
        a, b = b, a%b

    return b, int((x*y)/b)


#6.21 Pythagorean Triplets
def pythagorean_tri(m):
    lista = []
    for n in range(1, m):
        x, y = gcd_lcm(m, n)
        if x == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            lista.append((a, b, c))
    return lista


#6.22 Number conversion
def bin_int(n):
    string = ""
    while n > 0:
        resto = n%2
        string = str(int(resto)) + string
        n = n//2
    return string

def bin_frac(n):
    string = ""
    i = 0
    n, intg = modf(n)
    while n>0 and i<6:
        n = 2*n
        frac, intg = modf(n)
        string += str(int(intg))
        n = frac
        i+=1
    return string

def bin_float(n):
    frac, intg = modf(n)
    frac = bin_frac(frac)
    intg = bin_int(intg)
    return intg + "." + frac


def dec_int(string):
    new = string[::-1]
    dec = sum([eval(new[i])*(2**i) for i in range(len(string))])
    return dec


#6.23 Fibonacci Numbers
def fib_list(term):
    lista = [0, 1]
    for i in range(2, term):
        lista.append(lista[i-2]+lista[i-1])
    return lista


#6.24 Binary search
def binary_search(lista, item):
    index = -1
    a, b = 0, len(lista)-1
    while b >= a:
        n = int((b+a)/2)
        if item == lista[n]:
            index = n
            break
        elif item > lista[n]:
            a = n+1
        else:
            b = n-1
    return index


#6.25 Matrix Operations

def matrix_add(A, B):
    C = []
    for i in range(len(A)):
        line = []
        for j in range(len(A[0])):
            line.append(A[i][j] + B[i][j])
        C.append(line)
    return C

def matrix_prod(A, B):
    n = len(A)
    m = len(B[0])
    C = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(A[0])):
                C[i][j] += A[i][k]*B[k][j]
    return C

def matrix_transpose(A):
    B = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
    return B


if __name__ == "__main__":

    pass
    





