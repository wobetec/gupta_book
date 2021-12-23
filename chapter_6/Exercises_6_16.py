from math import factorial, sqrt, pi, sin

#01
def taylor_sin(x, tol):
    x = x * pi / 180
    soma = 0
    term = x
    n = 1
    while abs(term) > tol:
        soma += term
        term *= (- x**2 / (2*n*(2*n+1)))
        n += 1
    return soma

#02
def taylor_ln_1(x, tol):
    soma = 0
    term = x
    n = 1
    while abs(term) > tol:
        soma += term
        term *= (- x * n / (n+1))
        n += 1
    return soma

#03
def calc_pi(lim):
    p = 1
    for n in range(1, lim):
        p  = p * (4*n*n)/((2*n-1)*(2*n+1))
    return p*2


#04
def fourier(x, lim):
    soma = 0
    for n in range(1, lim):
        if n % 2 == 0:
            soma-=sin(n*x)/n
        else:
            soma+=sin(n*x)/n

    return 2*soma


if __name__ == '__main__':
    
    pass
