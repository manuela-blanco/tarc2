#Quando utilizamos uma variável em um escopo local, por exemplo em uma função, quando a chamada dessa função retornar, 
#caso o valor dessa variável não seja retornado, a variável é "perdida" e não podemos acessá-la do escopo global. 
#Por exemplo, no programa abaixo, temos uma variável "idade" no escopo global. Além disso, temos uma variável "idade" no 
#escopo local da função "get_idade()". Quando printamos o valor dessa variável no escopo global, o valor exibido é o 
#valor contido na variável de escopo global, pois não temos acesso à variável contida no escopo local da função. 

idade = 5

def get_idade():
  print("Entre com sua idade:")
  idade = input()

get_idade()
print("Idade:",idade)


#No entanto, caso a instrução "global" aparecesse antes da declaração da variável 
#dentro da função (escopo local), a variável seria considerada como uma variável global 
#e o resultado da execução do programa seria diferente. O programa consideraria que a atribuição 
#feita dentro da função mudaria o valor contido na variável global e o valor a ser printado ao 
#final seria o que foi passado como input.

idade = 5

def get_idade():
  global idade
  print("Entre com sua idade:")
  idade = input()

get_idade()
print("Idade:",idade)

#Além disso, caso a variável fosse retornada, teríamos como acessá-la através de 
#uma atribuição e o valor printado pelo programa seria aquele que foi passado como input.

idade = 5

def get_idade():
  print("Entre com sua idade:")
  idade = input()
  return idade

idade = get_idade()
print("Idade:",idade)