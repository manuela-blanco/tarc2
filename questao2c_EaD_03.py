#Questão 2)c

import matplotlib.pyplot as pt
import numpy as np

print("Entre com seu peso")
peso = input()
peso_original = peso
if(peso.replace('.', '').isdigit()):
  peso = float(peso_original)
else:
  print("Entre somente com números.")
  quit()
print("Entre com sua altura")
altura = input()
altura_original = altura
if(altura.replace('.', '').isdigit()):
  altura = float(altura_original)
else:
  print("Entre somente com números.")
  quit()

altura_turma = np.random.normal(1.75,0.05,30)
peso_turma = np.random.normal(70,3,30)

fig, ax = pt.subplots()
ax.set_xlabel('altura')
ax.set_ylabel('peso')

print('Você é o x azul.')
pt.plot(altura_turma, peso_turma, 'dr')
pt.plot(altura, peso, 'xb')