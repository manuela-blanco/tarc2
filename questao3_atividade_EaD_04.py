#Questão 3)

from urllib.request import urlopen
from bs4 import BeautifulSoup
pagina = urlopen("http://www.uniriotec.br")
arvore = BeautifulSoup(pagina.read(), "html5lib")
print(arvore.title)
print(arvore.h1)
print(arvore.p)

#Este programa acessa a página web "http://www.uniriotec.br", guarda os componentes html dessa página em uma variável objeto,
#e a partir dessa variável é possível acessar esses componentes html a partir dos seus atributos. Assim, o programa printa
#a tag título e seu conteúdo e a tag parágrafo e seu conteúdo. O programa também poderia printar a tag cabeçalho h1 e seu
# conteúdo, mas como ela não existe na página, o programa printa 'None'. 