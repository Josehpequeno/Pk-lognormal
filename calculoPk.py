import math

def I(x):
    z = x/(2**0.5)
    b = (0.5*(math.erf(z)))+0.5
    return b

media = 2.454439041#populacional
desvio = 0.5268861611#populacional
count = 495
k = round(1+(3.3*math.log10(count)))

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
while(a < max):
    m = round(a-0.001,3)
    if(b == max):
        l = round(b+0.001,3)
    else:
        l = b
    alpha = (math.log(m) - media)/desvio
    beta = (math.log(l) - media)/desvio
    pk = I(beta)-I(alpha)
    pk = round(pk,3)
    soma = round((pk+soma),3)
    if(b != max):
        print("Pk(",a,"<= Z <",b,") =",pk)
    else:
        print("Pk(",a,"<= Z <=",b,") =",pk)
    a = round(a+h, 3)
    b = round(b+h, 3)
print("\nCasos especiais:")
alpha = (math.log(min) - media)/desvio
pk = round(I(alpha),3)
print("Pk(",min,"< Z) =",pk)
soma = round((pk+soma),3)
beta = (math.log(max) - media)/desvio
pk = round(1-I(beta),3)
print("Pk(",max,"> Z) =",pk)
soma = round((pk+soma),3)
print("\nSoma dos valores", soma)
