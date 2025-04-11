while True:

    usuario = input("Digite o nome de usuário:")
    senha = input("Digite sua senha:")

    if usuario == senha:
        print("Senha inválida.")
    else:
        print("Login aceito")
        break

