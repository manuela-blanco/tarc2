#Questão 2)a

import numpy as np

array = np.arange(10)

print("Entre com um número para verificar se ele está na lista: ")
num = input()
if(num.isdigit()):
  num = int(num)
  print(array)
  if num in array:
    print("O número está contido na lista!")
  else:
    print("O número não está contido na lista.")
else:
  print("Entre somente com números.")
  quit()