# Ler uma variável de número inteiro e mostrar a tabuada desse número.

numero= int(input("digite seu numero: "))

print(f"sua taboada foi {numero}")

for i in range(1,11):
    print(f"{i} x {numero} = {i*numero}")

