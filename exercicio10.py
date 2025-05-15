#  Ler 10 valores e escrever quantos desses valores lidos
# estão no intervalo [10,20] (incluindo os
#  valores 10 e 20 no intervalo) e quantos deles estão
# fora deste intervalo.
dentro = 0
fora = 0

for i in range(10):
    valor = int(input("Digite um número: "))
    if 10 <= valor <= 20:
        dentro += 1
    else:
        fora += 1

print(f"A quantidade de números dentro do intervalo [10, 20] é {dentro}")
print(f"A quantidade de números fora do intervalo é {fora}")
