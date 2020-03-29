#Questão 2)b

from PIL import Image

print("Entre com o nome de duas cores em inglês para criar uma mistura: ")
print("Exemplo: yellow e lightblue resultam em verde")
cor_1 = str(input())
cor_2 = str(input())


imagem_1 = Image.new('RGB', (55, 20), color = cor_1)
imagem_1.save('img1.png')
imagem_2 = Image.new('RGB', (55, 20), color = cor_2)
imagem_2.save('img2.png')


mistura = Image.blend(imagem_1, imagem_2, 0.5)
mistura.save('mistura.png')

Image.open('mistura.png')