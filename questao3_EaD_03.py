#Questão 3)

import pandas as pd

estados = pd.Series(['Rio de Janeiro', 'São Paulo', 'Minas Gerais'], dtype= 'str')
populacao_total = pd.Series([6320000, 44040000, 20870000])

casos_corona = pd.Series([233, 745, 128])

base_corona = pd.DataFrame({'Estado': estados, 'População': populacao_total, 'Quantidade de casos de corona vírus': casos_corona})

base_corona['Porcentagem'] = base_corona['Quantidade de casos de corona vírus']/base_corona['População']


print('Entre com seu estado:')
estado = str(input())
if(base_corona['Estado'].str.contains(estado).any()):
  print('Porcentagem de casos no seu estado: ')
  print(base_corona['Porcentagem'][base_corona['Estado'] == estado])

else:
  print("O estado inserido não está na lista.")
  quit()