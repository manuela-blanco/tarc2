#Questão 5)

def collatz(number):
  if(number%2 == 0):
    print(number // 2)
    return number // 2
  else:
    print(3 * number + 1)
    return 3 * number + 1

def retorno_1():
  print("Entre com um número inteiro:")
  numero = input()
  if(numero.isdigit()):
    numero = int(numero)
  else:
    print("Entre somente com números inteiros.")
    quit()
  
  retorno = collatz(numero)
  while(retorno != 1):
    retorno = collatz(retorno)

retorno_1()

#Quando entramos com o número 7, temos como saída a sequência:
#7
#22
#11
#34
#17
#52
#26
#13
#40
#20
#10
#5
#16
#8
#4
#2
#1