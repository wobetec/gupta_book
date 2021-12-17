from random import randint
from time import perf_counter
from math import sqrt, factorial, pi, modf

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



if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    print(matrix_transpose(A))
    pass