# nome:
while True:
    nome = input("Digite seu nome (mais de 3 caracteres): ")

    if len(nome) > 3:
        print("Nome válido!")
        break
    else:
        print("Nome inválido! Tente novamente.")

# idade:
while True:
    idade = input("Digite sua idade (entre 0 e 150): ")

    if idade.isdigit():  # Verifica se a entrada é um número
        idade = int(idade)
        if 0 <= idade <= 150:
            print("Idade válida!")
            break
        else:
            print("Idade inválida! A idade deve ser entre 0 e 150.")
    else:
        print("Por favor, digite um número válido para a idade.")

# salário:
while True:
    salario = input("Digite seu salário (maior que 0): ")

    try:
        salario = float(salario)
        if salario > 0:
            print("Salário válido!")
            break
        else:
            print("Salário inválido! O salário deve ser maior que 0.")
    except ValueError:
        print("Por favor, digite um número válido para o salário.")

# sexo:
while True:
    sexo = input("Digite seu sexo ('f' para feminino ou 'm' para masculino): ").lower()

    if sexo == 'f' or sexo == 'm':
        print("Sexo válido!")
        break
    else:
        print("Sexo inválido! Digite 'f' ou 'm'.")

# estado civil:
while True:
    estado_civil = input(
        "Digite seu estado civil ('s' para solteiro, 'c' para casado, 'v' para viúvo ou 'd' para divorciado): ").lower()

    if estado_civil in ['s', 'c', 'v', 'd']:
        print("Estado civil válido!")
        break
    else:
        print("Estado civil inválido! Digite 's', 'c', 'v' ou 'd'.")
