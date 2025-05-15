# Modifique o exercício anterior para aceitar somente
# valores maiores que 0 para N. Caso o valor
# informado (para N) não seja maior que 0, deverá ser lido um novo valor para N.


numero = int(input("Digite um numero: "))


while numero <= 0:
    numero = int(input("Digite um numero novamente (maior que 0): "))


for i in range(1, numero + 1):
    print(i)

