a= 8000
b = 20000
ano = 0

while b > a:
    a += a * 0.03
    b += b * 0.015
    ano += 1

    print("Quantidade de anos", ano)
