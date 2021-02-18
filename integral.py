import math
def I(x):
    z = x/(2**0.5)
    b = (0.5*(math.erf(z)))+0.5
    return b

media = 6.738704938
desvio = 6.745522041
count = 495
k = round(1+(3.3*math.log10(count)))
#k = 1
print("Quantidade de classes",k)
print("Digite o valor mínimo")
min = float(input())
print("Digite o valor máximo")
max = float(input())
amplitude = max -min
h = amplitude/k
print("h:",h)
b = round(min +h,3)
a = min
soma = 0
while(a< max):
    alpha=(math.log(a)-(media+(desvio**2)))/desvio
    #print("alpha",alpha)
    if(b != max):
        l = b - 0.0001
    else:
        l = b
    beta =(math.log(l)-(media+(desvio**2)))/desvio
    print("\nLimites de",a,"á",l)
    #print("beta",beta)
    e = media+((desvio**2)/2)
    integral = math.exp(e)*(I(beta)-I(alpha))
    soma+=integral
    print("Resultado:",integral)
    a = round(a+h,3)
    b = round(b+h,3)
print("\nSoma dos valores",soma)
