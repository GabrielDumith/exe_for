#  Ler 5 valores, calcular e escrever a média aritmética
# desses valores lidos.

soma = 0
for i in range(5):
    numero = int(input("Digite um número: "))
    soma += numero
media = soma / 5

print(media)
