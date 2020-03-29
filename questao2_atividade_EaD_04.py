#Questão 2)

nome = "Manuela"

def entra_nome():
  print("Entre com seu nome: ")
  nome = input()

entra_nome()
print("Nome:",nome)

#Ao utilizar o mesmo nome para uma variável global e uma local,
#o programa considera que a variável local só existe no escopo da função onde está
#contida, e, caso a variável não seja retornada, ela deixa de existir no escopo global.
#Por isso, ao exucutar a instrução "print(nome)", o programa exibe o valor contido
#na variável global, e não considera que houve uma atribuição dentro da função
#que foi chamada.