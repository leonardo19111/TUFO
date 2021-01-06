a=int(input("Inserisci il coefficente con la x elevata alla seconda: "))
b=int(input("Inserisci il coefficente con la x: "))
c=int(input("Inserisci il coefficente del termine noto: "))


import math
def eq2grado(a,b,c):
    delta=(b*b)-(4*a*c)
    if delta < 0:
        return "Non esistono soluzioni"
    else:
        valsomma=(-b + math.sqrt(delta))/(2*a)
        valdifferenza=(-b - math.sqrt(delta))/(2*a)
        return valsomma,valdifferenza

    print(eq2grado(a,b,c))
