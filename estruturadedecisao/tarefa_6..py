numero1 = float(input("Digite um número:"))
numero2 = float(input("Digite outro número:"))
numero3 = float(input("Digite mais um número:"))
if numero1 > numero2 and numero1 > numero3:
    print(f"{numero1} foi o maior numero digitado.")
elif numero2 > numero1 and numero2 > numero3:
    print(f"{numero2} foi o maior numero digitado")
else:
    print(f"{numero3} foi o maior numero digitado.")
