from math import modf


#01
def octa_int(n):
    string = ""
    while n > 0:
        resto = n%8
        string = str(int(resto)) + string
        n = n//8
    return string

def octa_frac(n):
    string = ""
    i = 0
    n, intg = modf(n)
    while n>0 and i<8:
        n = 8*n
        frac, intg = modf(n)
        string += str(int(intg))
        n = frac
        i+=1
    return string

def octa_float(n):
    frac, intg = modf(n)
    frac = octa_frac(frac)
    intg = octa_int(intg)
    return intg + "." + frac


#02
def octa_to_dec(string):
    new = string[::-1]
    dec = sum([eval(new[i])*(8**i) for i in range(len(string))])
    return dec

if __name__ == "__main__":
    print(octa_to_dec("156"))
    pass

