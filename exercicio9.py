# Ler 10 valores e escrever quantos desses valores lidos
# são NEGATIVOS.

cont=0
for numero in range(10):
    numero=int(input("digite um numero: "))
    if numero<0:
        cont += 1


    print("Quantidade de números negativos:", cont)
