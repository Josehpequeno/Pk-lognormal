import math

#Aproximação polinomial da função erf().
def erf(z):
    t = 1/(1+(0.5*(math.fabs(z))))
    polinomial = -(z**2)-1.26551223+(1.00002368*t)+(0.37409196*(t**2))+(0.09678418*(t**3))-(0.18628806*(t**4)) + \
        (0.27886807*(t**5))-(1.13520398*(t**6)) + \
        (1.48851587*(t**7))-(0.82215223*(t**8))+(0.17087277*(t**9))
    eta = t*math.exp(polinomial)
    if(z >= 0):
        return 1 - eta
    else:
        return eta - 1

def I(x1):
    z = x1/(2**0.5)
    #b = 0.5*math.erfc(-z)
    b = (0.5*(erf(z)))+0.5 #resultado = 0.871811223086162
    #c = (0.5*(math.erf(z)))+0.5
    #a = (math.erf(z) + erf(z))/2 #resultado = 0.9900470588968668
    #b = (0.5*(math.erf(z)))+0.5
    #b = (b +c)/2 #resultado = 0.9900470588968667
    #b = round(b,8)
    #print("b:", b)
    return b

#media = 6.738704938
media = 2.454439041#populacional
#desvio = 6.745522041
desvio = 0.5268861611#populacional
count = 495
k = round(1+(3.3*math.log10(count)))
# k = 1
print("Quantidade de classes", k)
print("Digite o valor mínimo")
min = float(input())
print("Digite o valor máximo")
max = float(input())
amplitude = max - min
h = amplitude/k
print("h:", h)
b = round(min + h, 3)
a = min
soma = 0
e = media+((desvio**2)/2)
e = math.exp(e)
print("e:",e)
while(a < max):
    alpha = (math.log(a)-(media+(desvio**2)))/desvio
    if(b != max):
        l = round(b - 0.0001,4)
    else:
        l = b
    beta = (math.log(l)-(media+(desvio**2)))/desvio
    alpha = (math.log(alpha) - media)/desvio
    beta = (math.log(beta) - media)/desvio
    print("\nLimites de", a, "á", l)
    #print("alpha",alpha)
    #print("beta",beta)
    
    integral = e*(I(beta)-I(alpha))
    print("diferença",I(beta)-I(alpha))
    ####################### Aproximação do resultado para baixo
    #integral sem aproximação para baixo  #resultado = 1.1077
    #integral = round(integral-0.00005,4) #resultado = 1.107
    #integral = round(integral-0.0005,3) #resultado = 1.103
    #integral = round(integral-0.005,2) #resultado = 1.06
    #integral = round(integral-0.05,1) #resultado = 1.0
    soma = round(integral+soma,4)
    print("Resultado:", integral)
    a = round(a+h, 3)
    b = round(b+h, 3)
print("\nSoma dos valores", soma)
