import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


df = pd.read_csv('Preços MGLU3 Diário - Preços MGLU3 Diário.csv')

media = df['Fechamento'].mean()
moda = df['Fechamento'].mode()
mediana = df['Fechamento'].median()
minimo = df['Fechamento'].min()
maximo = df['Fechamento'].max()
amplitude = maximo - minimo
desvio_padrao = df['Fechamento'].std()
varianca = df['Fechamento'].var()
q1 = df['Fechamento'].quantile(0.25)
q2 = df['Fechamento'].quantile(0.5)
q3 = df['Fechamento'].quantile(0.75)

print(df)

print(f'\nMédia: {media}')
print(f'Mediana: {mediana}')
print(f'Moda: {moda}')
print(f'Mínimo: {minimo}')
print(f'Máximo: {maximo}' )
print(f'Amplitude: {amplitude}')
print(f'Desvio Padrão: {desvio_padrao}')
print(f'Variança da amostra: {varianca}')
print(f'1º quartil: {q1}')
print(f'2º quartil: {q2}')
print(f'3º quartil: {q3}')


#print(dir(df['Fechamento'].plot()))
df['Fechamento'].value_counts().plot.pie()
plt.show()